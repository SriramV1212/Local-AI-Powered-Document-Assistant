
# Local AI-Powered Document Assistant

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![DeepSeek](https://img.shields.io/badge/DeepSeek-8B-orange) ![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-brightgreen) ![LangChain](https://img.shields.io/badge/LangChain-RAG-blueviolet) ![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20DB-green) ![Status](https://img.shields.io/badge/Status-Active-success)

Welcome to the **Local AI-Powered Document Assistant** - a privacy-focused PDF analysis tool that runs entirely on your local machine. This application combines **DeepSeek 8B** (via Ollama) with **Retrieval-Augmented Generation (RAG)** to provide accurate answers to your PDF document questions without cloud dependencies.

---

## 🚀 **Features**

- **PDF Text Extraction**: Comprehensive text extraction using PyMuPDF
- **Semantic Search**: Vector embeddings with sentence-transformers/all-MiniLM-L6-v2
- **Local AI Processing**: DeepSeek 8B via Ollama for private document analysis
- **Vector Database**: ChromaDB for efficient document retrieval
- **Conversational Interface**: Streamlit chat interface with conversation history
- **Offline Capable**: All processing happens on your local machine

---

## 🛠️ **Tech Stack**

- **AI Model**: [DeepSeek 8B](https://ollama.ai/library/deepseek-r1) via Ollama
- **Embeddings**: sentence-transformers/all-MiniLM-L6-v2
- **Vector Database**: ChromaDB
- **Document Processing**: PyMuPDF
- **Text Splitting**: LangChain RecursiveCharacterTextSplitter
- **Web Interface**: Streamlit
- **Python Version**: 3.9+

---

## 📦 **Installation & Setup**

1. **Install Ollama and DeepSeek model**:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ollama pull deepseek-r1:8b
   ```

2. **Set up Python environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

---

## 🖥️ **Usage**

1. Upload a PDF document through the web interface
2. Wait for the document processing to complete (typically a few seconds)
3. Ask questions about the document content in natural language
4. Receive accurate, context-based answers from the local AI


---

## 📂 **Project Structure**

```
sriramv1212-local-ai-powered-document-assistant/
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── Chroma_DB/           # Auto-created vector database storage
└── README.md            # Project documentation
```

---

## 🔮 **Roadmap & Future Enhancements**

Planned improvements and features:

- [ ] Image extraction from PDFs
- [ ] Table data extraction and analysis
- [ ] Support for additional file types (DOCX, PPTX, CSV)
- [ ] Batch processing of multiple documents
- [ ] Improved chunking strategies with semantic awareness
- [ ] Advanced metadata handling
- [ ] Performance optimizations for large documents

---

## 🤝 **Contributing**

Contributions are welcome! If you have suggestions or improvements:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

For direct contact:

- Email: sriram.vivek@stonybrook.edu
- LinkedIn: https://www.linkedin.com/in/sriram-vivek-58a673269/

---

## 📄 **License**

MIT License - see [LICENSE](LICENSE) for details.

---

<p align="center">
  <em>⚡ Bringing powerful document analysis to your local machine ⚡</em>
</p>

