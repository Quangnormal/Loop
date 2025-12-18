import requests
import time

def run():
    URL = "https://mine.sttr.io/server/387558/poweraction"
    TOKEN = "VVI2bHIwYWU0SFRiWjhvdGVJV1pqdG41RFdjNzJmZU4="

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Origin": "https://minestrator.com",
        "Referer": "https://minestrator.com/",
        "User-Agent": (
            "Mozilla/5.0 (Linux; Android 10; K) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Mobile Safari/537.36"
        ),
    }

    data = {"poweraction": "start"}

    print("=== SEND START REQUEST ===", flush=True)
    r = requests.put(URL, headers=headers, json=data, timeout=10)

    print("STATUS:", r.status_code, flush=True)
    print("RESPONSE:", r.text, flush=True)

    return r.status_code, r.text


# Cho phép chạy độc lập (giữ nguyên hành vi code gốc)
if __name__ == "__main__":
    run()
