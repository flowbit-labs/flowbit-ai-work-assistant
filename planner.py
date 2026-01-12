from llm import chat
from prompts import PLANNER_SYSTEM, PLANNER_USER_TEMPLATE
from utils import now_local_string, compact_bullets

def make_plan(tasks: str) -> str:
    tasks = compact_bullets(tasks)
    user_prompt = PLANNER_USER_TEMPLATE.format(now=now_local_string(), tasks=tasks)
    return chat(PLANNER_SYSTEM, user_prompt, temperature=0.4)
