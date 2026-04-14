import json
from datetime import datetime

def save_history(history, filename="logs/chat_history.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
