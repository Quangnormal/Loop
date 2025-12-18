from flask import Flask
from main import run_job
import threading

app = Flask(__name__)
lock = threading.Lock()

@app.route("/")
def index():
    if lock.locked():
        return "Job is running", 429

    with lock:
        run_job()

    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
