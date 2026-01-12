import os
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("FLOWBIT_MODEL", "gpt-4o-mini")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()

if not OPENAI_API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY. Add it to your .env file.")
