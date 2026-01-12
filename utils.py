from datetime import datetime

def now_local_string() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def compact_bullets(lines: str) -> str:
    # Ensures nice spacing when user pastes messy task lists
    cleaned = []
    for line in lines.splitlines():
        line = line.strip()
        if not line:
            continue
        cleaned.append(line)
    return "\n".join(cleaned)
