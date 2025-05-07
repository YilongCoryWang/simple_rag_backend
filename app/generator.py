from openai import OpenAI
from app.config import LLM_API_KEY
from app.config import LLM_BASE_URL

def generate_answer(query: str, docs: list[str]) -> str:
    context = "\n".join(docs)
    prompt = f"""Please answer the user's question based on the following document content:

Document Content:
{context}

User Question:
{query}

Please answer concisely and accurately.
"""
    print("prompt")
    print(prompt)
    print("send api request")
    client = OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )

    return response.choices[0].message.content
