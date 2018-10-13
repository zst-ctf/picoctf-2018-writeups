#!/usr/bin/env python3
from solve_extract import xor_zip_bytes, tohex, attack_block

ciphertext = bytes.fromhex("5468697320697320616e204956343536bade59109764febea2c7750a4dae94dc9d494afe7d2f6f65fb1396791585bc03001275db3d5dc7666a39a5b1159e261a7bce4dd133a77c975cbba1ddb3751bc69f88ebbf9d2ca59cda28230eddb23e16")

# Block 0 - #16: b'\x16\xf7\xb0m\xb94vpd\x1a\xbf\xf3\xdf\xd1\xff\x8a' True
C0 = b'This is an IV456'
I0 = b'\x16\xf7\xb0m\xb94vpd\x1a\xbf\xf3\xdf\xd1\xff\x8a'
P0 = b''

# Block 1 - #16: b'/J\x1c\x00E\x1b\x1dA\x0c\x0b\x02sv\x16RC' True
C1 = b'\xba\xdeY\x10\x97d\xfe\xbe\xa2\xc7u\nM\xae\x94\xdc'
I1 = b'/J\x1c\x00E\x1b\x1dA\x0c\x0b\x02sv\x16RC'
P1 = b'{"username": "gu'

# Block 2 - #16: b'\xdf\xad-2\xbbD\xdc\xdb\xda\xb7\x1cx(\xdd\xb6\xe6' True
C2 = b'\x9dIJ\xfe}/oe\xfb\x13\x96y\x15\x85\xbc\x03'
I2 = b'\xdf\xad-2\xbbD\xdc\xdb\xda\xb7\x1cx(\xdd\xb6\xe6'
P2 = b'est", "expires":'

# Block 3 - #16: b'\xbdkx\xceM\x1fBU\xca>\xa6N7\xa9\x9c!' True
C3 = b'\x00\x12u\xdb=]\xc7fj9\xa5\xb1\x15\x9e&\x1a'
I3 = b'\xbdkx\xceM\x1fBU\xca>\xa6N7\xa9\x9c!'
P3 = b' "2000-01-07", "'

# Block 4 - #16: b'ia*\xbaY0\xae\x08H\x03\x85\x93s\xffJi' True
C4 = b'{\xceM\xd13\xa7|\x97\\\xbb\xa1\xdd\xb3u\x1b\xc6'
I4 = b'ia*\xbaY0\xae\x08H\x03\x85\x93s\xffJi'
P4 = b'is_admin": "fals'

# Block 5 - #16: b'\x1e\xec0\xdc>\xaaq\x9aQ\xb6\xac\xd0\xbex\x16\xcb' True
C5 = b'\x9f\x88\xeb\xbf\x9d,\xa5\x9c\xda(#\x0e\xdd\xb2>\x16'
I5 = b'\x1e\xec0\xdc>\xaaq\x9aQ\xb6\xac\xd0\xbex\x16\xcb'
P5 = b'e"}\r\r\r\r\r\r\r\r\r\r\r\r\r'

Cx = [C0, C1, C2, C3, C4, C5]
Ix = [I0, I1, I2, I3, I4, I5]
Px = [P0, P1, P2, P3, P4, P5]


def get_full_ciphertext():
    return b''.join(Cx)


def get_full_text():
    full = b''
    for block in range(1, 6):
        Px[block] = xor_zip_bytes(Ix[block], Cx[block-1])
        full += Px[block]
    return full


def change_text(block, newtext):
    delta = xor_zip_bytes(Px[block], newtext)
    # print(Cx[block-1])
    
    # control the ciphertext only
    Cx[block-1] = xor_zip_bytes(Cx[block-1], delta)
    # print(Cx[block-1])

    # Afterwhich the cipher of the previous will affect
    # the intermediate value too. So, update it here.
    c, i, p = attack_block(get_full_ciphertext(), block_number=block-1)
    Ix[block-1] = i
    Px[block-1] = p

if __name__ == '__main__':
    assert (ciphertext) == get_full_ciphertext()

    print("Original")
    print(get_full_text())
    print(get_full_ciphertext())
    print(tohex(get_full_ciphertext()))
    print()

    print("Bit Flip Block 4")
    change_text(4, b'is_admin":  "tru')
    print()

    print("Bit Flip Block 3")
    change_text(3, b' "2040-01-07", "')
    print()

    print("Bit Flip Block 2")
    change_text(2, b'vst", "expires":')
    print()

    print("Bit Flip Block 1")
    change_text(1, b'{"username": "ad')
    print()

    # change_text(1, b'{"username": "ad')
    # change_text(2, b'min", "expires":')
    # change_text(3, b' "2040-01-07", "')
    # change_text(4, b'is_admin":  "tru')
    # change_text(4, b'is_admin":  "tru')

    print("Final Payload")
    print(get_full_text())
    print(tohex(get_full_ciphertext()))
