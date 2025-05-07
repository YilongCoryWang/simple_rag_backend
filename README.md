# 🔍 Simple RAG Backend (Retrieval-Augmented Generation)

This is a lightweight backend for building RAG (Retrieval-Augmented Generation) applications using:

- 🧠 SentenceTransformer for text embedding
- 🔎 FAISS for vector similarity search
- 🤖 Large Language Models (DeepSeek / OpenAI)
- ⚡ FastAPI for a simple RESTful interface

---

## 🚀 Features

- Upload and index PDF documents
- Perform semantic search over document content
- Generate answers to user questions based on retrieved passages
- Modular design for easy extension

---

## 📦 Dependencies

```bash
# Python >= 3.9 recommended
pip install -r requirements.txt
```

## 🛠️ How to run

```bash
mv .env.templeate .env
# Edit .env file and fill in your own LLM's base url and api key
uvicorn app.main:app --reload
```

## 📤 Upload & Index a PDF

```http
POST /upload-pdf/
Form field: file (PDF file)
```

## ❓ Ask a Question

```http
GET /query/?question=What is a transformer?
```

## 📂 Project Structure

```graphql
simple_rag_backend/
├── app/
│ ├── main.py # FastAPI app with endpoints
│ ├── loader.py # PDF text extraction
│ ├── embedder.py # SentenceTransformer-based embeddings
│ ├── indexer.py # FAISS vector index
│ ├── retriever.py # Similarity search
│ └── generator.py # LLM-based answer generation
```

## 📄 License

MIT License
