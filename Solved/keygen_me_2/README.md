# keygen-me-2
Reversing - 750 points

## Challenge 
> The software has been updated. Can you find us a new product key for the program in /problems/keygen-me-2_1_762036cde49fef79146a706d0eda80a3



## Hint
> z3

## Solution

Similar to keygen-me-1, input of 16 char product key (digit and uppercase)


In `validate_key()`:
- Functions `key_constraint_xx()` are called from `01` to `12`
- Returns true if all != 0

I have reversed the code from Retargetable Decompiler as follows:

```C

int32_t mod(int64_t a, int32_t b) {
    return a % b
}

int32_t key_constraint_01(char * str, int32_t length) {
    int value = ord(str[0]) + ord(str[1])
    return mod(value, 36) == 14;
}

int32_t key_constraint_02(char * str, int32_t length) {
    int value = ord(str[2]) + ord(str[3])
    return mod(value, 36) == 24;
}

int32_t key_constraint_03(char * str, int32_t length) {
    int value = ord(str[2]) - ord(str[0]);
    return mod(value, 36) == 6;
}

int32_t key_constraint_04(char * str, int32_t length) {
    int value = ord(str[1]) + ord(str[3]) + ord(str[5]);
    return mod(value, 36) == 4;
}

int32_t key_constraint_05(char * str, int32_t length) {
    int value = ord(str[2]) + ord(str[4]) + ord(str[6]);
    return mod(value, 36) == 13;
}

int32_t key_constraint_06(char * str, int32_t length) {
    int value = ord(str[3]) + ord(str[4]) + ord(str[5]);
    return mod(value, 36) == 22;
}

int32_t key_constraint_07(char * str, int32_t length) {
    int value = ord(str[6]) + ord(str[8]) + ord(str[10]);
    return mod(value, 36) == 31;
}

int32_t key_constraint_08(char * str, int32_t length) {
    int value = ord(str[1]) + ord(str[4]) + ord(str[7]);
    return mod(value, 36) == 7;
}

int32_t key_constraint_09(char * str, int32_t length) {
    int value = ord(str[9]) + ord(str[12]) + ord(str[15]);
    return mod(value, 36) == 20;
}

int32_t key_constraint_10(char * str, int32_t length) {
    int value = ord(str[13]) + ord(str[14]) + ord(str[15]);
    return mod(value, 36) == 12;
}

int32_t key_constraint_11(char * str, int32_t length) {
    int value = ord(str[8]) + ord(str[9]) + ord(str[10]);
    return mod(value, 36) == 27;
}

int32_t key_constraint_12(char * str, int32_t length) {
    int value = ord(str[7]) + ord(str[12]) + ord(str[13]);
    return mod(value, 36) == 23;
}
```


---

### Using Z3 to solve for constraints

#### Installation Instructions

- http://flolac.iis.sinica.edu.tw/flolac15/_media/download:manual-install-z3.pdf

TLDR:
1. Download your OS binary from [here](https://github.com/Z3Prover/bin/tree/master/nightly)
2. Unzip and open a terminal
3. `export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin`
4. `export PYTHONPATH=~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin/python`
5. Run your script.

#### Solving

Good examples of using Z3

- https://rolandsako.wordpress.com/2016/02/17/playing-with-z3-hacking-the-serial-check/
- https://speakerdeck.com/milkmix/using-z3-to-solve-crackme
- https://ericpony.github.io/z3py-tutorial/guide-examples.htm

I created a script to solve for it with all the ***modulo key constraints***, as well as constrain it to a number between 0 to 35 inclusive.

```bash
$ python z3solve.py 
    [key__1 = 22,
     key__10 = 20,
     key__9 = 7,
     key__11 = 0,
     key__7 = 17,
     key__12 = 15,
     key__5 = 28,
     key__2 = 34,
     key__15 = 34,
     key__13 = 27,
     key__6 = 11,
     key__8 = 0,
     key__3 = 26,
     key__0 = 28,
     key__4 = 4,
     key__14 = 23]
 ```

Now we can plug it into the charset and combine it

    >>> key = [''] * 16
    >>> key[1] = 22;
    >>> key[10] = 20;
    >>> key[9] = 7;
    >>> key[11] = 0;
    >>> key[7] = 17;
    >>> key[12] = 15;
    >>> key[5] = 28;
    >>> key[2] = 34;
    >>> key[15] = 34;
    >>> key[13] = 27;
    >>> key[6] = 11;
    >>> key[8] = 0;
    >>> key[3] = 26;
    >>> key[0] = 28;
    >>> key[4] = 4;
    >>> key[14] = 23;
    >>> ''.join(list(map(lambda x: "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[x], key)))
    'SMYQ4SBH07K0FRNY'

Solved.

    $ ./activate SMYQ4SBH07K0FRNY
    Product Activated Successfully: picoCTF{c0n5tr41nt_50lv1nG_15_W4y_f45t3r_3846045707}

## Flag

	picoCTF{c0n5tr41nt_50lv1nG_15_W4y_f45t3r_3846045707}
