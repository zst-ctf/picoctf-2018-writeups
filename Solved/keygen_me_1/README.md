# keygen-me-1
Reversing - 400 points

## Challenge 
> Can you generate a valid product key for the validation [program](activate) in /problems/keygen-me-1_1_8eb35cc7858ff1d2f55d30e5428f30a7

## Solution

#### Decompile the program

For `check_valid_char()`
- Return true if digit ('0' to '9')
- Return true if uppercase letter ('A' to 'Z') 

For `check_valid_key()`
- Check if length == 16
- Each char passes `check_valid_char()`

For `ord()`
- if digit, return digit as integer
    - ie. 0 to 9 returns 0 through 9
- if letter, return (ASCII value - 55)
    - ie. A to Z returns 10 through 35

The function does the following


	// Address range: 0x8048771 - 0x804881d
	int32_t validate_key(char * str) {
	    // 0x8048771
	    int32_t v1; // bp-28
	    int32_t v2 = &v1; // 0x8048775
	    int32_t v3 = (int32_t)str;
	    int32_t v4 = strlen(str) - 1; // 0x80487cc
	    int64_t v5 = 0;
	    if (v4 > 0) {
	        int32_t v6 = 0;
	        *(int32_t *)(v2 - 16) = (int32_t)*(char *)(v6 + v3);
	        int32_t v7 = g2 + 16; // 0x80487b0
	        int32_t v8 = v6 + 1; // 0x80487bc
	        int32_t v9 = (ord() + 1) * v8; // 0x80487c2
	        while (v8 != v4) {
	            // 0x8048799
	            v6 = v8;
	            *(int32_t *)(v7 - 16) = (int32_t)*(char *)(v6 + v3);
	            v7 = g2 + 16;
	            v8 = v6 + 1;
	            v9 += (ord() + 1) * v8;
	            // continue -> 0x8048799
	        }
	        // 0x80487c9
	        v2 = v7;
	        v5 = v9;
	        // branch -> 0x80487d4
	    }
	    uint64_t v10 = 0x38e38e39 * (v5 & 0xffffffff) / 0x800000000; // 0x80487e26
	    int32_t v11 = (int32_t)v5 + -4 * ((int32_t)(8 * v10) + (int32_t)v10); // ebx
	    *(int32_t *)(v2 - 16) = (int32_t)*(char *)(v4 + v3);
	    int32_t v12 = ord(); // 0x8048808
	    return (int32_t)(v11 == v12) | v12 & -256;
	}


Simplified

```C
int32_t validate_key(char * str) {
    int32_t len = strlen(str) - 1;
    int64_t sum = 0;
    if (len > 0) {
        sum = (ord(str[0]) + 1) * 1; // 0x80487c2
        int32_t i = 1; // 0x80487bc
        while (i != len) {
            sum += (ord(str[i]) + 1) * (i+1);
            i++;
        }
    }
    uint64_t v10 = 0x38e38e39 * (sum & 0xffffffff) / 0x800000000; // 0x80487e26
    int32_t v11 = sum + -36 * v10; // ebx
    int32_t v12 = ord(str[len]); // 0x8048808
    return (int32_t)(v11 == v12);//-256;
}
```

---

After this, I did some debugging in `./debug.c`

```C
int32_t validate_key(char * str) {
    int32_t len = strlen(str) - 1;
    int64_t sum = 0;
    if (len > 0) {
        sum = (ord(str[0]) + 1) * 1; // 0x80487c2
        int32_t i = 1; // 0x80487bc
        while (i != len) {
            printf("Debug sum (%d): %d \n", i, sum);
            sum += (ord(str[i]) + 1) * (i+1);
            i++;
        }
    }

    // v10 = sum / 36
    uint64_t v10 = 0x38e38e39 * (sum & 0xffffffff) / 0x800000000; 
    
    // thus, v10 gets remainder of the division = sum % 36
    int32_t v11 = sum + -36 * v10; // ebx

    // Hence, check if remainder = final char
    int32_t v12 = ord(str[len]); // 0x8048808

    printf("Debug sum (end): %d \n", sum);
    printf("Debug v10: %d \n", v10);
    printf("Debug v11: %d \n", v11);

    return (int32_t) (v11 == v12);//-256;
}
```

**The sum of the 15 chars of product key is divided by 36 and the remainder is checked against the 16th char.**

My input value of `AAAABBBBCCCCDDDD` gives remainder of 8


	Input AAAABBBBCCCCDDDD
	Debug sum (end): 1556
	Debug v10: 43
	Debug v11: 8
	Result 0

So changing to `AAAABBBBCCCCDDD8` should be valid

	Input AAAABBBBCCCCDDD8
	Debug sum (end): 1556
	Debug v10: 43
	Debug v11: 8
	Result 1

## Flag


And now plug into the program

	$ ./activate 'AAAABBBBCCCCDDD8'
	Product Activated Successfully: picoCTF{k3yg3n5_4r3_s0_s1mp13_3718231394}
