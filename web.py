from flask import Flask
from main import run_job
import time
import os
import threading

app = Flask(__name__)

LOCK = threading.Lock()
INTERVAL = 4 * 60 * 60  # 4 tiếng (giây)
STATE_FILE = "last_run.txt"


def get_last_run():
    if not os.path.exists(STATE_FILE):
        return 0
    try:
        with open(STATE_FILE, "r") as f:
            return float(f.read().strip())
    except:
        return 0


def set_last_run(ts):
    with open(STATE_FILE, "w") as f:
        f.write(str(ts))


@app.route("/")
def index():
    if LOCK.locked():
        return "Job is running", 429

    now = time.time()
    last_run = get_last_run()

    if now - last_run < INTERVAL:
        remain = int((INTERVAL - (now - last_run)) / 60)
        return f"Too soon. Wait ~{remain} minutes", 200

    with LOCK:
        run_job()
        set_last_run(now)

    return "OK - job executed", 200


@app.route("/health")
def health():
    return "alive", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
