import os
from datetime import datetime

def save_report(content, folder="reports"):
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename
