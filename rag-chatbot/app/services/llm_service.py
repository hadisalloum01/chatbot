import openai
from app.core.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def ask_llm(context: str, question: str) -> str:
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()
