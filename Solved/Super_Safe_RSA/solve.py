#!/usr/bin/env python3

# https://gist.github.com/ofaurax/6103869014c246f962ab30a513fb5b49
# Took from SO
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

# given
c = 19186016582318064428291303425902140901883296951420146438700416985707104860040269
n = 22104805049219253595688155381445306328126758057554593510365000451311355387636863
e = 65537

# https://en.wikipedia.org/wiki/RSA_numbers#RSA-768
p = 144258603536574599963220429490269382037
q = 153230410577313765737534565937792115989699


phi = (p - 1) * (q - 1)
d = modinv(e, phi)

m = pow(c, d, n)

msg = bytes.fromhex(hex(m)[2:]).decode()
print(msg)
