import os
import requests


def get_matches(bytes_data):
    with open("audio.wav", "wb") as f:
        f.write(bytes_data)

    PORT = 45678
    ENDPOINT = "/search"

    url = f"http://0.0.0.0:{PORT}{ENDPOINT}"
    headers = {"Content-Type": "application/json"}

    path = os.path.abspath("audio.wav")
    data = {"data": [{"uri": path}]}

    # try:
    response = requests.post(url, headers=headers, json=data)
    content = response.json()
    os.remove("audio.wav")
    matches = content["data"]["docs"][0]["chunks"][0]["matches"]
    print(matches)
    # matches = content["data"][0].docs[0].matches
    # return content["data"]["docs"][0]["matches"]
    return matches
    # except Exception:
        # return []
