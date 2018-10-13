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

int main() {
    int result = validate_key("AAAABBBBCCCCDDDD");
    printf("Result %d", result);
    return 0;
}
