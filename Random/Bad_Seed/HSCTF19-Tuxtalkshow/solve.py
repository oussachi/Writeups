from pwn import *
from time import *
import ctypes

# Load the C standard library
libc = ctypes.CDLL(None)  # On Unix-like systems, this loads the C library

seed = libc.time(0)
libc.srand(seed)  # Set the seed to 0, for example
p = process("./tuxtalkshow")

val_list = [0] * 6
val_list[0] = 0x79
val_list[1] = 0x12c97f
val_list[2] = 0x135f0f8
val_list[3] = 0x74acbc6
val_list[4] = 0x56c614e
val_list[5] = 0xffffffe2

for i in range(6):
    temp = libc.rand()
    val_list[i] -= (temp % 10) - 1

    sum_ = 0
for i in range(6):
    sum_ += val_list[i]

sum_ = sum_ & 0xffffffff
p.recv()
p.sendline(str(sum_))
print(p.recv())