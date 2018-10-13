#!/usr/bin/env python
from z3 import *

filename = "map1.txt"
filename = "map2.txt"

with open(filename, 'r') as f:
    cipher, chalbox = eval(f.read())

length, gates, check = chalbox

# Create bit vectors
b = []
total_length = check[0] + 1
for count in range(total_length):
    b.append(BitVec(str(count), 1))


# verify() constraints
s = Solver()

for i, (name, args) in enumerate(gates):
    position = i + length

    if name == 'true':
        # b.append(1)
        s.add(b[position] == 1)
    else:
        u1 = b[args[0][0]] ^ args[0][1]
        u2 = b[args[1][0]] ^ args[1][1]
        if name == 'or':
            # b.append(u1 | u2)
            s.add(b[position] == (u1 | u2))
        elif name == 'xor':
            # b.append(u1 ^ u2)
            s.add(b[position] ==(u1 ^ u2))
        else:
            raise Exception("unknown gate")

s.add((b[check[0]] ^ check[1]) == 1)

# Solve
# https://z3prover.github.io/api/html/classz3py_1_1_model_ref.html
if s.check():
    m = s.model()

    sequence = ''
    key = 0
    for item in b:
        name = str(item)
        value = str(m[item])
        # print(name, value)

        sequence += value

        bit_pos = int(name)
        value = int(value)
        if bit_pos < length:
            key |= value << bit_pos

    print 'sequence', sequence
    print 'key', key



