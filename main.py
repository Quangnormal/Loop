import requests

def run_job():
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

    r = requests.put(URL, headers=headers, json=data, timeout=10)

    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    run_job()
