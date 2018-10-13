#!/usr/bin/env python3
import socket

def bin_to_ascii(n):
    n = n.replace(" ", "")
    n = int(n, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

def dec_to_ascii(n):
    num = n.strip().split(' ')
    ascii = list(map(lambda x: chr(int(x)), num))
    return ''.join(ascii)

def oct_to_ascii(n):
    num = n.strip().split(' ')
    ascii = list(map(lambda x: chr(int(x, 8)), num))
    return ''.join(ascii)

def hex_to_ascii(n):
    return bytes.fromhex(n).decode()

s = socket.socket()
s.connect(('2018shell2.picoctf.com', 14390))

while True:
    data = s.recv(4096).decode().strip()
    if not data:
        continue

    print("Received:", data)

    if 'Please give me the ' in data:
        number = data.split("Please give me the ")[1].split('as')[0].strip()

        choice = input(f'Decode {number}: ').strip()
        if choice == 'b':
            decoded = bin_to_ascii(number)
        elif choice == 'o':
            decoded = oct_to_ascii(number)
        elif choice == 'd':
            decoded = dec_to_ascii(number)
        elif choice == 'h':
            decoded = hex_to_ascii(number)

        print(">> Decoded:", decoded)
        s.send(decoded.encode() + b'\n')        

    if '>' in data:
        payload = payloads.pop(0)
        print('Sending:', payload)
        s.send(payload)

    if 'flag' in data:
        quit()
