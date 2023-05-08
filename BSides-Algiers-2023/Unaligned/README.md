
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

# Flag

`shellmates{SOrRY_fOR_f0RciBLy_Untify1ng_0ne_g4DGet_CoN$}`
