
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
