//
// This file was generated by the Retargetable Decompiler
// Website: https://retdec.com
// Copyright (c) 2018 Retargetable Decompiler <info@retdec.com>
//

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ------------------------ Structures ------------------------

struct _IO_FILE {
    int32_t e0;
};

// ------------------- Function Prototypes --------------------

int32_t check_valid_char(void);
int32_t check_valid_key(char * a1);
int32_t key_constraint_01(char * a1, int32_t a2);
int32_t key_constraint_02(char * a1, int32_t a2);
int32_t key_constraint_03(char * a1, int32_t a2);
int32_t key_constraint_04(char * a1, int32_t a2);
int32_t key_constraint_05(char * a1, int32_t a2);
int32_t key_constraint_06(char * a1, int32_t a2);
int32_t key_constraint_07(char * a1, int32_t a2);
int32_t key_constraint_08(char * a1, int32_t a2);
int32_t key_constraint_09(char * a1, int32_t a2);
int32_t key_constraint_10(char * a1, int32_t a2);
int32_t key_constraint_11(char * a1, int32_t a2);
int32_t key_constraint_12(char * a1, int32_t a2);
int32_t mod(int64_t a1, int32_t a2);
int32_t ord(unsigned char a1);
int32_t print_flag(void);
int32_t validate_key(char * str);

// --------------------- Global Variables ---------------------

int32_t g1 = 0; // ebp
struct _IO_FILE * g2 = NULL;

// ------------------------ Functions -------------------------

// Address range: 0x80485fb - 0x8048686
int32_t print_flag(void) {
    struct _IO_FILE * file = fopen("flag.txt", "r"); // 0x8048619
    if (file != NULL) {
        int32_t str = 0; // bp-80
        fgets((char *)&str, 64, file);
        printf("%s", &str);
        fclose(file);
        // branch -> 0x8048673
    } else {
        // 0x804862a
        puts("Flag File is Missing.");
        // branch -> 0x8048673
    }
    // 0x8048673
    int32_t result; // 0x8048685
    if (*(int32_t *)20 != *(int32_t *)20) {
        // 0x804867f
        __stack_chk_fail();
        int32_t * v1;
        result = (int32_t)&v1;
        // branch -> 0x8048684
    } else {
        result = 0;
    }
    // 0x8048684
    return result;
}

// Address range: 0x8048686 - 0x80486b8
int32_t check_valid_char(void) {
    // 0x8048686
    char v1;
    if (v1 <= 47) {
        // 0x80486b1
        // branch -> 0x80486b6
        // 0x80486b6
        return 0;
    }
    // 0x8048698
    if (v1 > 57 != (unsigned char)(v1 - 65) > 25) {
        // 0x80486b6
        return 1;
    }
    // 0x80486b1
    // branch -> 0x80486b6
    // 0x80486b6
    return 0;
}

// Address range: 0x80486b8 - 0x804870a
int32_t ord(unsigned char a1) {
    // 0x80486b8
    if (a1 <= 47) {
        // 0x80486ee
        puts("Found Invalid Character!");
        exit(0);
        // UNREACHABLE
    }
    // 0x80486ca
    int32_t result;
    if (a1 > 57) {
        // 0x80486d9
        if (a1 > 90) {
            // 0x80486ee
            puts("Found Invalid Character!");
            exit(0);
            // UNREACHABLE
        }
        // 0x80486e5
        result = (int32_t)a1 - 55;
        // branch -> 0x8048708
    } else {
        // 0x80486d0
        result = (int32_t)a1 - 48;
        // branch -> 0x8048708
    }
    // 0x8048708
    return result;
}

// Address range: 0x804870a - 0x8048771
int32_t check_valid_key(char * a1) {
    int32_t result = 0; // 0x8048770
    if (a1 != NULL) {
        char v1 = *a1;
        if (v1 != 0) {
            int32_t v2; // bp-20
            int32_t v3 = &v2; // 0x8048733
            int32_t v4 = 0;
            int32_t v5; // 0x8048747
            while (true) {
                // 0x804872f
                *(int32_t *)(v3 - 4) = (int32_t)v1;
                if ((char)check_valid_char() != 0) {
                    // 0x8048747
                    v5 = v4 + 1;
                    char v6 = *(char *)(v5 + (int32_t)a1);
                    if (v6 == 0) {
                        // break -> 0x804875f
                        break;
                    }
                    v3 = 4;
                    v1 = v6;
                    v4 = v5;
                    // continue -> 0x804872f
                    continue;
                }
            }
            // 0x804875f
            result = v5 == 16 ? 16 : 0;
            // branch -> 0x804876f
        } else {
            result = 0;
        }
    }
    // 0x804876f
    return result;
}

// Address range: 0x8048771 - 0x8048796
int32_t mod(int64_t a1, int32_t a2) {
    int32_t v1 = (0x100000000 * (int64_t)((int32_t)a1 >> 31) | a1 & 0xffffffff) % (int64_t)a2; // 0x804877b
    return (v1 >= 0 ? 0 : a2) + v1;
}

// Address range: 0x8048796 - 0x80487eb
int32_t key_constraint_01(char * a1, int32_t a2) {
    int32_t v1 = ord(*a1); // 0x80487aa
    char v2 = *(char *)((int32_t)a1 + 1); // 0x80487bb
    int32_t v3 = mod((int64_t)(v1 + ord(v2)), 36); // 0x80487d8
    return (int32_t)(v3 == 14) | v3 & -256;
}

// Address range: 0x80487eb - 0x8048843
int32_t key_constraint_02(char * a1, int32_t a2) {
    int32_t v1 = (int32_t)a1; // 0x80487f2
    int32_t v2 = ord(*(char *)(v1 + 2)); // 0x8048802
    int32_t v3 = mod((int64_t)(v2 + ord(*(char *)(v1 + 3))), 36); // 0x8048830
    return (int32_t)(v3 == 24) | v3 & -256;
}

// Address range: 0x8048843 - 0x804889a
int32_t key_constraint_03(char * a1, int32_t a2) {
    int32_t v1 = ord(*(char *)((int32_t)a1 + 2)); // 0x804885a
    int32_t v2 = mod((int64_t)(v1 - ord(*a1)), 36); // 0x8048887
    return (int32_t)(v2 == 6) | v2 & -256;
}

// Address range: 0x804889a - 0x804890f
int32_t key_constraint_04(char * a1, int32_t a2) {
    int32_t v1 = (int32_t)a1; // 0x80488a1
    int32_t v2 = ord(*(char *)(v1 + 1)); // 0x80488b1
    int32_t v3 = ord(*(char *)(v1 + 3)); // 0x80488cc
    int32_t v4 = mod((int64_t)(v2 + v3 + ord(*(char *)(v1 + 5))), 36); // 0x80488fc
    return (int32_t)(v4 == 4) | v4 & -256;
}

// Address range: 0x804890f - 0x8048984
int32_t key_constraint_05(char * a1, int32_t a2) {
    int32_t v1 = (int32_t)a1; // 0x8048916
    int32_t v2 = ord(*(char *)(v1 + 2)); // 0x8048926
    int32_t v3 = ord(*(char *)(v1 + 4)); // 0x8048941
    int32_t v4 = mod((int64_t)(v2 + v3 + ord(*(char *)(v1 + 6))), 36); // 0x8048971
    return (int32_t)(v4 == 13) | v4 & -256;
}

// Address range: 0x8048984 - 0x80489f9
int32_t key_constraint_06(char * a1, int32_t a2) {
    int32_t v1 = (int32_t)a1; // 0x804898b
    int32_t v2 = ord(*(char *)(v1 + 3)); // 0x804899b
    int32_t v3 = ord(*(char *)(v1 + 4)); // 0x80489b6
    int32_t v4 = mod((int64_t)(v2 + v3 + ord(*(char *)(v1 + 5))), 36); // 0x80489e6
    return (int32_t)(v4 == 22) | v4 & -256;
}

// Address range: 0x80489f9 - 0x8048a6e
int32_t key_constraint_07(char * a1, int32_t a2) {
    int32_t v1 = (int32_t)a1; // 0x8048a00
    int32_t v2 = ord(*(char *)(v1 + 6)); // 0x8048a10
    int32_t v3 = ord(*(char *)(v1 + 8)); // 0x8048a2b
    int32_t v4 = mod((int64_t)(v2 + v3 + ord(*(char *)(v1 + 10))), 36); // 0x8048a5b
    return (int32_t)(v4 == 31) | v4 & -256;
}

// Address range: 0x8048a6e - 0x8048ae3
int32_t key_constraint_08(char * a1, int32_t a2) {
    int32_t v1 = (int32_t)a1; // 0x8048a75
    int32_t v2 = ord(*(char *)(v1 + 1)); // 0x8048a85
    int32_t v3 = ord(*(char *)(v1 + 4)); // 0x8048aa0
    int32_t v4 = mod((int64_t)(v2 + v3 + ord(*(char *)(v1 + 7))), 36); // 0x8048ad0
    return (int32_t)(v4 == 7) | v4 & -256;
}

// Address range: 0x8048ae3 - 0x8048b58
int32_t key_constraint_09(char * a1, int32_t a2) {
    int32_t v1 = (int32_t)a1; // 0x8048aea
    int32_t v2 = ord(*(char *)(v1 + 9)); // 0x8048afa
    int32_t v3 = ord(*(char *)(v1 + 12)); // 0x8048b15
    int32_t v4 = mod((int64_t)(v2 + v3 + ord(*(char *)(v1 + 15))), 36); // 0x8048b45
    return (int32_t)(v4 == 20) | v4 & -256;
}

// Address range: 0x8048b58 - 0x8048bcd
int32_t key_constraint_10(char * a1, int32_t a2) {
    int32_t v1 = (int32_t)a1; // 0x8048b5f
    int32_t v2 = ord(*(char *)(v1 + 13)); // 0x8048b6f
    int32_t v3 = ord(*(char *)(v1 + 14)); // 0x8048b8a
    int32_t v4 = mod((int64_t)(v2 + v3 + ord(*(char *)(v1 + 15))), 36); // 0x8048bba
    return (int32_t)(v4 == 12) | v4 & -256;
}

// Address range: 0x8048bcd - 0x8048c42
int32_t key_constraint_11(char * a1, int32_t a2) {
    int32_t v1 = (int32_t)a1; // 0x8048bd4
    int32_t v2 = ord(*(char *)(v1 + 8)); // 0x8048be4
    int32_t v3 = ord(*(char *)(v1 + 9)); // 0x8048bff
    int32_t v4 = mod((int64_t)(v2 + v3 + ord(*(char *)(v1 + 10))), 36); // 0x8048c2f
    return (int32_t)(v4 == 27) | v4 & -256;
}

// Address range: 0x8048c42 - 0x8048cb7
int32_t key_constraint_12(char * a1, int32_t a2) {
    int32_t v1 = (int32_t)a1; // 0x8048c49
    int32_t v2 = ord(*(char *)(v1 + 7)); // 0x8048c59
    int32_t v3 = ord(*(char *)(v1 + 12)); // 0x8048c74
    int32_t v4 = mod((int64_t)(v2 + v3 + ord(*(char *)(v1 + 13))), 36); // 0x8048ca4
    return (int32_t)(v4 == 23) | v4 & -256;
}

// Address range: 0x8048cb7 - 0x8048dfc
int32_t validate_key(char * str) {
    int32_t len = strlen(str); // 0x8048cc3
    if ((char)key_constraint_01(str, len) == 0 || (char)key_constraint_02(str, len) == 0 || (char)key_constraint_03(str, len) == 0 || (char)key_constraint_04(str, len) == 0 || (char)key_constraint_05(str, len) == 0 || (char)key_constraint_06(str, len) == 0 || (char)key_constraint_07(str, len) == 0 || (char)key_constraint_08(str, len) == 0 || (char)key_constraint_09(str, len) == 0 || (char)key_constraint_10(str, len) == 0 || (char)key_constraint_11(str, len) == 0) {
        // 0x8048df5
        // branch -> 0x8048dfa
        // 0x8048dfa
        return 0;
    }
    // 0x8048dd8
    if ((char)key_constraint_12(str, len) != 0) {
        // 0x8048dfa
        return 1;
    }
    // 0x8048df5
    // branch -> 0x8048dfa
    // 0x8048dfa
    return 0;
}

// Address range: 0x8048dfc - 0x8048ebf
int main(int argc, char ** argv) {
    setvbuf(g2, NULL, 2, 0);
    if (argv <= (char **)1) {
        // 0x8048e26
        puts("Usage: ./activate <PRODUCT_KEY>");
        // branch -> 0x8048eb5
        // 0x8048eb5
        return -1;
    }
    // 0x8048e3d
    int32_t v1;
    int32_t * v2 = (int32_t *)(v1 + 4); // 0x8048e43
    if ((char)check_valid_key((char *)*v2) == 0) {
        // 0x8048e55
        puts("Please Provide a VALID 16 byte Product Key.");
        // branch -> 0x8048eb5
        // 0x8048eb5
        return -1;
    }
    // 0x8048e6c
    int32_t result; // 0x8048ebe
    if ((char)validate_key((char *)*v2) != 0) {
        // 0x8048e9b
        printf("Product Activated Successfully: ");
        print_flag();
        result = 0;
        // branch -> 0x8048eb5
    } else {
        // 0x8048e84
        puts("INVALID Product Key.");
        result = -1;
        // branch -> 0x8048eb5
    }
    // 0x8048eb5
    return result;
}

// --------------- Dynamically Linked Functions ---------------

// void __stack_chk_fail(void);
// void exit(int status);
// int fclose(FILE * stream);
// char * fgets(char * restrict s, int n, FILE * restrict stream);
// FILE * fopen(const char * restrict filename, const char * restrict modes);
// int printf(const char * restrict format, ...);
// int puts(const char * s);
// int setvbuf(FILE * restrict stream, char * restrict buf, int modes, size_t n);
// size_t strlen(const char * s);

// --------------------- Meta-Information ---------------------

// Detected compiler/packer: gcc (5.4.0)
// Detected functions: 19
// Decompilation date: 2018-10-06 10:08:50