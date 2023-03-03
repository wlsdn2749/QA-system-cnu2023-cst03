import requests
import json

def get_table(idx: int = 2):
    url = f"http://127.0.0.1:8001/board/{idx}"

    response = requests.get(url, verify=False)
    print(response.json())
    print(response.text)
    return response.json()