from llm import chat
from prompts import WRITER_SYSTEM, WRITER_USER_TEMPLATE

def rewrite_text(text: str, goal: str = "clarity", tone: str = "professional and friendly") -> str:
    user_prompt = WRITER_USER_TEMPLATE.format(goal=goal, tone=tone, text=text)
    return chat(WRITER_SYSTEM, user_prompt, temperature=0.5)
