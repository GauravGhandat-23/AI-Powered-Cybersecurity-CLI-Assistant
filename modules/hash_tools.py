import hashlib
import os

def file_hashes(file_path):
    if not os.path.exists(file_path):
        return {"error": "File not found"}

    sha256 = hashlib.sha256()
    md5 = hashlib.md5()

    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
            md5.update(chunk)

    return {
        "md5": md5.hexdigest(),
        "sha256": sha256.hexdigest()
    }
