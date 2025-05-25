from pwn import *

p = remote("challenge.nahamcon.com", 32713)

found = 0
while(not found):
    data = p.recv()
    if(b"flag{" in data):
        print(data)
        found = 1
    else:
        p.sendline()