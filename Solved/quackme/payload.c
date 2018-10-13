#include <stdio.h>

/*
             sekrutBuffer:
08048858         db  0x29 ; ')'                                                 ; DATA XREF=do_magic+126
08048859         db  0x06 ; '.'
0804885a         db  0x16 ; '.'
0804885b         db  0x4f ; 'O'
0804885c         db  0x2b ; '+'
0804885d         db  0x35 ; '5'
0804885e         db  0x30 ; '0'
0804885f         db  0x1e ; '.'
08048860         db  0x51 ; 'Q'
08048861         db  0x1b ; '.'
08048862         db  0x5b ; '['
08048863         db  0x14 ; '.'
08048864         db  0x4b ; 'K'
08048865         db  0x08 ; '.'
08048866         db  0x5d ; ']'
08048867         db  0x2b ; '+'
08048868         db  0x50 ; 'P'
08048869         db  0x14 ; '.'
0804886a         db  0x5d ; ']'
0804886b         db  0x00 ; '.'
0804886c         db  0x19 ; '.'
0804886d         db  0x17 ; '.'
0804886e         db  0x59 ; 'Y'
0804886f         db  0x52 ; 'R'
08048870         db  0x5d ; ']'
08048871         db  0x00 ; '.'
*/

char * sekrutBuffer = "\x29\x06\x16\x4f\x2b\x35\x30\x1e\x51\x1b\x5b\x14\x4b\x08\x5d\x2b\x50\x14\x5d\x00\x19\x17\x59\x52\x5d\x00";

char greetingMessage[] = "You have now entered the Duck Web, and you're in for a honkin' good time.\nCan you figure out my trick?";

int main()
{
    for (int index = 0; index < 25; index++) {
        char payload = (greetingMessage[index] ^ sekrutBuffer[index]);
        printf("%c", payload);
    }
    return 0;
}
