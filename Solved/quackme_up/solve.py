#!/usr/bin/python
from pwn import *
import string

def encrypt(plaintext):
    p = process('./main')
    p.sendline(plaintext)

    p.recvuntil("Here's your ciphertext: ")
    ciphertext = p.recvline().strip()

    p.close()
    return ciphertext

# Gather a mapping of chars to encoded chars
lookup_table = dict()
for ch in string.printable:
    key = encrypt(ch)
    if key:
        lookup_table[key] = ch

# Decrypt
quackme = "11 80 20 E0 22 53 72 A1 01 41 55 20 A0 C0 25 E3 20 30 00 45 05 35 40 65 C1"
flag = ""
for enc in quackme.split(" "):
    flag += lookup_table[enc]

print(flag)
