import subprocess
import shlex

def run_command(command):
    try:
        result = subprocess.run(
            shlex.split(command),
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.stdout if result.stdout else result.stderr
    except Exception as e:
        return f"Error running command: {e}"
