from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

_client = OpenAI(api_key=OPENAI_API_KEY)

def chat(system: str, user: str, temperature: float = 0.4) -> str:
    resp = _client.chat.completions.create(
        model=MODEL,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return resp.choices[0].message.content.strip()
