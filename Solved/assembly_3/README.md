# assembly-3
Reversing - 400 points

## Challenge 
> What does asm3(0xfac0f685,0xe0911505,0xaee1f319) return? Submit the flag as a hexadecimal value (starting with '0x')

## Hint
> more(?) [registers](https://wiki.skullsecurity.org/index.php?title=Registers)


## Solution


Assembly

    asm3:
        push    ebp
        mov     ebp,esp
        mov eax,0x27
        xor al,al
        mov ah,BYTE PTR [ebp+0xb]
        sal ax,0x10
        sub al,BYTE PTR [ebp+0xc]
        add ah,BYTE PTR [ebp+0xf]
        xor ax,WORD PTR [ebp+0x12]
        mov esp, ebp
        pop ebp
        ret

Psuedocode

    // asm3(0xfac0f685,0xe0911505,0xaee1f319)
    // param2 = ebp+0x10 == 0xaee1f319 or 
    // param2 = ebp+0x0c == 0xe0911505 or 
    // param1 = ebp+0x08 == 0xfac0f685
    // return = ebp+0x04

    asm3:
        push    ebp
        mov     ebp,esp
        mov eax,0x27               ; eax == 0x0000_0027    
        xor al,al                  ; al = 0,       hence eax == 0x0000_0000 
        mov ah,BYTE PTR [ebp+0xb]  ; ah = 0xfa,    hence eax == 0x0000_fa00
        sal ax,0x10                ; ax <<= 16,    hence eax == 0x0000_0000
        sub al,BYTE PTR [ebp+0xc]  ; al -= 0x05,   hence eax == 0x0000_00fb
        add ah,BYTE PTR [ebp+0xf]  ; ah += 0xe0,   hence eax == 0x0000_e0fb
        xor ax,WORD PTR [ebp+0x12] ; ax ^= 0xaee1, hence eax == 0x0000_4e1a
        mov esp, ebp
        pop ebp
        ret

I made use of pwntools to understand the stack

    $ python
    >>> from pwn import *
    >>> buf = 'BASE' + 'RETN' + p32(0xfac0f685) + p32(0xe0911505) + p32(0xaee1f319)

    >>> buf[0xb]
    '\xfa'

    >>> buf[0xc]
    '\x05'

    >>> buf[0xf]
    '\xe0'

    >>> buf[0x12]
    '\xe1'

    >>> hex(0x100-0x05) # byte underflow from subtraction
    '0xfb'

    >>> hex(0xe0fb ^ 0xaee1)
    '0x4e1a'

References:
- https://reverseengineering.stackexchange.com/questions/18735/is-it-possible-to-access-the-higher-part-of-the-32-bit-and-64-bit-registers-if
- https://wiki.skullsecurity.org/index.php?title=Registers#16-bit_and_8-bit_Registers


## Flag

    0x4e1a
