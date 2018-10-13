#!/usr/bin/env python3
from z3 import *

key = IntVector("key", 16)
s = Solver()

# KEYGEN CONSTRAINTS

key_constraint_01 = key[0] + key[1]
s.add(key_constraint_01 % 36 == 14)

key_constraint_02 = key[2] + key[3]
s.add(key_constraint_02 % 36 == 24)

key_constraint_03 = key[2] - key[0]
s.add(key_constraint_03 % 36 == 6)

key_constraint_04 = key[1] + key[3] + key[5]
s.add(key_constraint_04 % 36 == 4)

key_constraint_05 = key[2] + key[4] + key[6]
s.add(key_constraint_05 % 36 == 13)

key_constraint_06 = key[3] + key[4] + key[5]
s.add(key_constraint_06 % 36 == 22)

key_constraint_07 = key[6] + key[8] + key[10]
s.add(key_constraint_07 % 36 == 31)

key_constraint_08 = key[1] + key[4] + key[7]
s.add(key_constraint_08 % 36 == 7)

key_constraint_09 = key[9] + key[12] + key[15]
s.add(key_constraint_09 % 36 == 20)

key_constraint_10 = key[13] + key[14] + key[15]
s.add(key_constraint_10 % 36 == 12)

key_constraint_11 = key[8] + key[9] + key[10]
s.add(key_constraint_11 % 36 == 27)

key_constraint_12 = key[7] + key[12] + key[13]
s.add(key_constraint_12 % 36 == 23)

# NUMBER CONSTRAINT
def addConstraintBetweenXandY(solver, group, x, y):
	for i in range(0, len(group)):
		solver.add(group[i] >= x, group[i] < y)

for x in range(16):
	addConstraintBetweenXandY(s, key, 0, 35)

# SOLVE
if s.check():
	m = s.model()
	print(m)
