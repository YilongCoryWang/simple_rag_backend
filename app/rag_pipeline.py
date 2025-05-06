from app.embedder import model
from app.retriever import search
from app.generator import generate_answer

def rag_pipeline(question: str, index, texts):
    query_vec = model.encode([question])[0]
    docs = search(index, query_vec, texts)
    print("docs")
    print(docs)
    return generate_answer(question, docs)
