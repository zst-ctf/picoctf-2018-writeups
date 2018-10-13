#!/usr/bin/env python3
from functools import lru_cache

# Memoized function
@lru_cache(maxsize=None)
def calc(var_24):
    if (var_24 <= 0x4):
        var_14 = var_24 * var_24 + 0x2345
    else:
        var_14 = calc(var_24 - 0x5) * 0x1234 + (calc(var_24 - 0x1) - calc(var_24 - 0x2)) + (calc(var_24 - 0x3) - calc(var_24 - 0x4));
    return var_14

# Calculate upwards to allow cache to initialise
# This prevents the error - RecursionError: maximum recursion depth exceeded in comparison
for i in range(0x19965):
	calc(i)

# Finally do calculation
# Limit it to 64-bit integer size
print("Result:", calc(0x19965) & (2**64 - 1))
