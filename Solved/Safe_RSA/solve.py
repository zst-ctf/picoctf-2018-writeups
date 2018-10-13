#!/usr/bin/env python3
import gmpy2
import binascii

gmpy2.get_context().precision=200

c = 2205316413931134031046440767620541984801091216351222789180573437837873413848819848972069088625959518346568495824756225842751786440791759449675594790690830246158935538568387091288002447511390259320746890980769089692036188995150522856413797

# https://stackoverflow.com/a/356187
# gmpy2 has gmpy2.iroot to compute integer roots

m = gmpy2.iroot(c, 3)[0]
print(m)

assert pow(m,3) == c

# Convert to ascii
def hex_pair(x):
    return ('0' * (len(x) % 2)) + x

m_hex = '{:x}'.format(m)
m_hex = hex_pair(m_hex)
msg = binascii.unhexlify(m_hex)
print(msg.decode())
