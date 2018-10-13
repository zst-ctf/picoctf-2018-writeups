#!/usr/bin/python3
import binascii
import base64
import json

BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE).encode()
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def xor_zip_bytes(bytearray1, bytearray2):
    final = b''
    for a, b in zip(bytearray1, bytearray2):
        final += bytes([a ^ b])
    return final

# initial data
cookie = "NqOtxYG8kL09alb9GtCw8VDdfd+2CEcFSTp7NtM8wx57jtHbBLD3RL7dGfWylX3A8P3LortMHUa0NTzKLeegf4tSG6JSunf7IzXdKWIAukM="
cookie_dict = {'admin': 0, 'password': 'hi', 'username': 'hi'}

# original values
ciphertext = base64.b64decode(cookie)
plaintext = json.dumps(cookie_dict, sort_keys=True).encode()
plaintext = pad(plaintext)

# Check length is same
assert len(ciphertext) - 16 == len(plaintext)  # 16 bytes longer because of IV prepended

# target value
cookie_dict['admin'] = 1
new_plaintext = json.dumps(cookie_dict, sort_keys=True).encode()
new_plaintext = pad(new_plaintext)

# calculate new value
# extra block because of IV
delta = xor_zip_bytes(plaintext, new_plaintext)
delta += b'\x00' * (BLOCK_SIZE * 1)

new_ciphertext = xor_zip_bytes(delta, ciphertext)
new_cookie = base64.b64encode(new_ciphertext)

'''
print(plaintext)
print(new_plaintext)
print(ciphertext)
print(new_ciphertext)
'''

print("New Cookie:")
print("session="+new_cookie.decode())

