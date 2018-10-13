#!/usr/bin/python3

from Crypto import Random
from Crypto.Cipher import AES
import sys
import time
import binascii
import base64


def xor_zip_bytes(bytearray1, bytearray2):
    final = b''
    for a, b in zip(bytearray1, bytearray2):
        final += bytes([a ^ b])
    return final

def get_keystream(send, recv):
    plaintext = send.encode() + b".txt"
    ciphertext = base64.b64decode(recv)
    assert len(plaintext) == len(ciphertext)
    keystream = xor_zip_bytes(plaintext, ciphertext)

    print("plaintext:", plaintext)
    print("ciphertext:", ciphertext)
    print("keystream:", keystream)
    print()

    return keystream

def calculate_share_code(plaintext, keystream):
    plaintext = plaintext.encode() + b".txt"
    ciphertext = xor_zip_bytes(plaintext, keystream)
    share_code = base64.b64encode(ciphertext)

    print("Share code:", share_code)
    print()

    return share_code


def debug():
    send = "AAAAAAAAAAAAAAAAAAAAAAAAA"
    recv = "iKUkWi+QdHLy49jMpwUb2IilJFovkHRy8ozt9ZI="
    keystream = get_keystream(send, recv)

    send2 = "BBBBBBBBBBBBBBBBBBBBBBBBB" 
    recv2 = "i6YnWSyTd3Hx4NvPpAYY24umJ1ksk3dx8Yzt9ZI="
    keystream2 = get_keystream(send2, recv2)

    assert keystream == keystream2
    assert recv2 == calculate_share_code(send2, keystream2).decode()


def main():
    send = "AAAAAAAAAAAAAAAAAAAAAAAAA"
    recv = "aDRAiN4cUN+kAiCJOlEo+mg0QIjeHFDfpG0VsA8="

    filename = 'flag_e734862f2a5dffdcd8c8'

    keystream = get_keystream(send, recv)
    calculate_share_code(filename, keystream).decode()

if __name__ == '__main__':
    main()
