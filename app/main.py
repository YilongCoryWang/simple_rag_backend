from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
# from app.retriever import search
# from app.generator import generate_answer
from app.loader import extract_text_from_pdf
from app.embedder import embed_texts
from app.indexer import build_faiss_index
from app.rag_pipeline import rag_pipeline

app = FastAPI()

index = None
texts = None

@app.get("/")
def hello():
    return {"message": "RAG backend is running."}

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        raw_text = extract_text_from_pdf(contents)

        global index, texts
        # split by paragraph
        texts = [t.strip() for t in raw_text.split('\n') if t.strip()]
        embeddings = embed_texts(texts)
        print("embeddings")
        index = build_faiss_index(embeddings)
        print(index)

        return {"msg": "PDF uploaded and indexed", "chunks": len(texts)}
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )
    
@app.get("/query/")
async def query_pdf(question: str):
    from app.embedder import model
    global index, texts
    if index is None:
        return {"error": "No document uploaded"}
    # query_vec = model.encode([question])[0]
    # results = search(index, query_vec, texts)
    answer = rag_pipeline(question, index, texts)
    return {"answer": answer}

