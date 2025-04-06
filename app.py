import streamlit as st
import fitz
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from ollama import chat


if "messages" not in st.session_state:
    st.session_state.messages = [{'role': 'system', 'content': """You are a factual assistant for Document Question/Answering.
                                             Answer ONLY using the provided context. 
                                             If the context doesn't contain the answer, just say you don't have enough information.
                                             Keep responses concise and directly supported by the context."""}]


def process_pdf_and_create_vector_store(pdf_path):
    
    doc = fitz.open(pdf_path)
    text = ""
    for num in range(len(doc)):
        page = doc.load_page(num)
        page_text = page.get_textpage().extractText()
        text += page_text + "\n"
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)
    chunks = text_splitter.split_text(text)
    valid_chunks = [chunk for chunk in chunks if chunk.strip()]
    
   
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    persistent_directory = os.path.join(current_dir, "Chroma_DB", "db1")
    
    vector_store = Chroma(
        collection_name="DataBase1",
        embedding_function=embeddings,
        persist_directory=persistent_directory
    )
    
    vector_store.reset_collection()

    vector_store.add_texts(
        texts=valid_chunks,
        ids=(str(id) for id in range(1, len(valid_chunks)+1))
        )
    return vector_store


st.title("Document Q/A Assistant")


uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_file is not None:
    
    temp_file_path = os.path.join(os.getcwd(), "temp_upload.pdf")
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    
    vector_store = process_pdf_and_create_vector_store(temp_file_path)
    
    
    os.remove(temp_file_path)
    
    st.success("Document processed successfully! You can now ask questions.")
    
    
    for message in st.session_state.messages[1:]:  
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    
    if prompt := st.chat_input("Ask a question about the document"):
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
       
        results = vector_store.search(
            query=prompt,
            search_type="similarity",
            k=3,
        )
        
        context = ""
        for res in results:
            context += res.page_content
        
        query = f"{prompt}. The context to answer this question is {context}"
        
        
        temp_messages = st.session_state.messages.copy()
        temp_messages.append({'role': 'user', 'content': query})
        
        
        response = chat(
            'deepseek-r1:8b',
            messages=temp_messages
        )

        result = response.message.content.split("</think>")[1]
        
       
        st.session_state.messages.append({"role": "assistant", "content": result})
        
        
        with st.chat_message("assistant"):
            st.markdown(result)
else:
    st.info("Please upload a PDF document to get started.")

    
