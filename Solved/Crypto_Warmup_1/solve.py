#!/usr/bin/env python3

import string
charset = string.ascii_lowercase

key = 'thisisalilkey'
key = list(map(lambda x: charset.index(x), list(key)))

enc = 'llkjmlmpadkkc'
enc = list(map(lambda x: charset.index(x), list(enc)))

flag = ''
for a, b in zip(key, enc):
    index = b - a
    if (index < 0):
        index += 26
    flag += charset[index]

print("picoCTF{" + flag.upper() + "}")
