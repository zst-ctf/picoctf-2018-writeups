#!/usr/bin/env python3
import socket
import binascii
import time
from multiprocessing.pool import ThreadPool


def tohex(text):
    return binascii.hexlify(text)


def is_valid(payload):
    # try until successful
    while True:
        try:
            s = socket.socket()
            s.connect(('2018shell2.picoctf.com',6246))
            s.send(payload + b'\n')
            # print(payload)

            while True:
                data = s.recv(4096).decode().strip()
                # print("Received:", data)
                if not data:
                    # print("Received:", data)
                    return False
                if 'invalid padding' in data:
                    return False
                if 'd=json.loads(unpad(cookie2decoded))' in data:
                    # error decoding, means padding was verified
                    return True
            break
        except:
            time.sleep(0.5)
    return False


def get_block(x, b):
    return x[16 * b:16 * (b + 1)]


def xor_each_byte(byte_array, xor_value):
    xored_array = b''
    for b in byte_array:
        xored_array += bytes([b ^ xor_value])
    return xored_array


def xor_zip_bytes(bytearray1, bytearray2):
    final = b''
    for a, b in zip(bytearray1, bytearray2):
        final += bytes([a ^ b])
    return final


def attack_block(ciphertext, prefix=b'', block_number=2):
    IV = prefix # get_block(ciphertext, 0)
    C1 = get_block(ciphertext, 1 + (block_number - 2))
    C2 = get_block(ciphertext, 2 + (block_number - 2))


    # Start up threads
    pool = ThreadPool(processes=50)

    # Get intermediate state of block 2
    progress = b''
    while len(progress) < 16:
        # count is the padding bytes
        count = len(progress) + 1

        async_results = []

        # For all possible bytes, create a payload
        for ch in range(256):
            # To begin with, we choose C1'[1..15] to be random bytes, and C1'[16] to be 00
            
            # We found the last byte by fiddling with C1' until we produced something with valid padding,
            # and in doing so were able to infer that the final byte of P'2 was 01. 

            # We now choose C1'[1..14] to be random bytes, C1'[15] to be the byte 00, 
            # and C1'[16] to be a byte chosen so as to make P2'[16] == 02:

            ch = bytes([ch])
            C1p = b'A' * (16-count) + ch + xor_each_byte(progress, count)
            payload = tohex(IV+C1p+C2)

            # Send jobs to threads: result = is_valid(payload)
            async_result = pool.apply_async(is_valid, (payload,))
            async_results.append((ch, async_result))
            
        # Get results
        for ch, async_result in async_results:
            valid = async_result.get()
            if valid:
                intermediate_ch = bytes([ch[0] ^ count])
                progress = intermediate_ch + progress
                print(f"\rBlock {block_number} - #{count}: {progress} {valid}", end='')
                break

    # Get plaintext of block 2
    I2 = progress
    P2 = xor_zip_bytes(I2, C1)

    print()
    print(f"Solved C{block_number}: {C2}")
    print(f"Solved I{block_number}: {I2}")
    print(f"Solved P{block_number}: {P2}")

    return C2, I2, P2


if __name__ == '__main__':
    ciphertext = bytes.fromhex("5468697320697320616e204956343536bade59109764febea2c7750a4dae94dc9d494afe7d2f6f65fb1396791585bc03001275db3d5dc7666a39a5b1159e261a7bce4dd133a77c975cbba1ddb3751bc69f88ebbf9d2ca59cda28230eddb23e16")
    # print(attack_block(ciphertext, block_number=2))
    
    total_blocks = len(ciphertext) // 16

    for block in range(4, total_blocks):
        attack_block(ciphertext, block_number=block)
        
