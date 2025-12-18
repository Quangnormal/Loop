from flask import Flask
import main
import threading

app = Flask(__name__)

lock = threading.Lock()

@app.route("/", methods=["GET", "HEAD"])
def trigger():
    with lock:
        status, text = main.run()

    return f"""
    <h3>Triggered Minecraft Start</h3>
    <b>Status:</b> {status}<br>
    <b>Response:</b><br>
    <pre>{text}</pre>
    """, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
