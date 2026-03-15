from pwn import *
from time import *
import ctypes   

# Load the C standard library
libc = ctypes.CDLL(None)  # On Unix-like systems, this loads the C library

seed = libc.time(0)
libc.srand(seed)  # Set the seed to 0, for example
p = process("./prepared")

for i in range(0x32):
    val = libc.rand()
    p.recv()
    p.sendline(str(val % 100))
print(p.recv())
p.interactive()