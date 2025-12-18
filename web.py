from flask import Flask
from main import run_job
import threading

app = Flask(__name__)
LOCK = threading.Lock()


@app.route("/")
def index():
    if LOCK.locked():
        return "Job is running", 429

    with LOCK:
        run_job()

    return "OK - request sent", 200


@app.route("/health")
def health():
    return "alive", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
