from llm import chat
from prompts import REVIEW_SYSTEM, REVIEW_USER_TEMPLATE
from utils import now_local_string, compact_bullets

def end_of_day_review(wins: str, open_loops: str) -> str:
    wins = compact_bullets(wins)
    open_loops = compact_bullets(open_loops)
    user_prompt = REVIEW_USER_TEMPLATE.format(
        now=now_local_string(),
        wins=wins,
        open_loops=open_loops,
    )
    return chat(REVIEW_SYSTEM, user_prompt, temperature=0.4)
