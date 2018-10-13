/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int32_t ord(char v1) {
    if (v1 > 57) {
        if (v1 > 90) {
            puts("Found Invalid Character!");
            exit(0);
        }
        return (v1 - 55); // alphabet
    } else {
        return (v1 - 48); // digit
    }
}


int32_t mod(int64_t a, int32_t b) {
    return a % b;
}

int32_t key_constraint_01(char * str, int32_t length) {
    int value = ord(str[0]) + ord(str[1]);
    printf("key_constraint_01: %d == 14\n", mod(value, 36));
    return mod(value, 36) == 14;
}

int32_t key_constraint_02(char * str, int32_t length) {
    int value = ord(str[2]) + ord(str[3]);
    printf("key_constraint_02: %d == 24\n", mod(value, 36));
    return mod(value, 36) == 24;
}

int32_t key_constraint_03(char * str, int32_t length) {
    int value = ord(str[2]) - ord(str[0]);
    printf("key_constraint_03: %d == 6\n", mod(value, 36));
    return mod(value, 36) == 6;
}

int32_t key_constraint_04(char * str, int32_t length) {
    int value = ord(str[1]) + ord(str[3]) + ord(str[5]);
    printf("key_constraint_04: %d == 4\n", mod(value, 36));
    return mod(value, 36) == 4;
}

int32_t key_constraint_05(char * str, int32_t length) {
    int value = ord(str[2]) + ord(str[4]) + ord(str[6]);
    printf("key_constraint_05: %d == 13\n", mod(value, 36));
    return mod(value, 36) == 13;
}

int32_t key_constraint_06(char * str, int32_t length) {
    int value = ord(str[3]) + ord(str[4]) + ord(str[5]);
    printf("key_constraint_06: %d == 22\n", mod(value, 36));
    return mod(value, 36) == 22;
}

int32_t key_constraint_07(char * str, int32_t length) {
    int value = ord(str[6]) + ord(str[8]) + ord(str[10]);
    printf("key_constraint_07: %d == 31\n", mod(value, 36));
    return mod(value, 36) == 31;
}

int32_t key_constraint_08(char * str, int32_t length) {
    int value = ord(str[1]) + ord(str[4]) + ord(str[7]);
    printf("key_constraint_08: %d == 7\n", mod(value, 36));
    return mod(value, 36) == 7;
}

int32_t key_constraint_09(char * str, int32_t length) {
    int value = ord(str[9]) + ord(str[12]) + ord(str[15]);
    printf("key_constraint_09: %d == 20\n", mod(value, 36));
    return mod(value, 36) == 20;
}

int32_t key_constraint_10(char * str, int32_t length) {
    int value = ord(str[13]) + ord(str[14]) + ord(str[15]);
    printf("key_constraint_10: %d == 12\n", mod(value, 36));
    return mod(value, 36) == 12;
}

int32_t key_constraint_11(char * str, int32_t length) {
    int value = ord(str[8]) + ord(str[9]) + ord(str[10]);
    printf("key_constraint_11: %d == 27\n", mod(value, 36));
    return mod(value, 36) == 27;
}

int32_t key_constraint_12(char * str, int32_t length) {
    int value = ord(str[7]) + ord(str[12]) + ord(str[13]);
    printf("key_constraint_12: %d == 23\n", mod(value, 36));
    return mod(value, 36) == 23;
}


char charset[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
char KEY[16] = "AAAABBBBCCCCDDDD";

void do_check() {
    if (key_constraint_01(KEY, 0) && 
        key_constraint_02(KEY, 0) && 
        key_constraint_03(KEY, 0) && 
        key_constraint_04(KEY, 0) && 
        key_constraint_05(KEY, 0) && 
        key_constraint_06(KEY, 0) && 
        key_constraint_07(KEY, 0) && 
        key_constraint_08(KEY, 0) && 
        key_constraint_09(KEY, 0) && 
        key_constraint_10(KEY, 0) && 
        key_constraint_11(KEY, 0) && 
        key_constraint_12(KEY, 0)) {
        printf("Success %s \n", KEY);
        exit(0);
    }
}
int main() {
    do_check();
    return 0;
}
