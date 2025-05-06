def search(index, query_embedding, texts, top_k=3):
    import numpy as np
    D, I = index.search(np.array([query_embedding]).astype('float32'), top_k)
    return [texts[i] for i in I[0]]