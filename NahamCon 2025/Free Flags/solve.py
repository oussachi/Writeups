import base64
import string

def has_non_valid_char(text):
    return any(c not in "abcdef0123456789" for c in text)

f = open("free_flags.txt")

for line in f:
    vals = line.split("  ")
    for val in vals:
        flag = val.split("{")[1].split("}")[0]
        if(not has_non_valid_char(flag)):
            print("flag{"+flag+'}')