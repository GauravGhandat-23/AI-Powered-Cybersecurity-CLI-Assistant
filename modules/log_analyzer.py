import os

def read_log_file(file_path, max_chars=12000):
    if not os.path.exists(file_path):
        return None, "Log file not found."

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read(max_chars)

    return content, None
