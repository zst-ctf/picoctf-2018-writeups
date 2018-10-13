# assembly-0
Reversing - 150 points

## Challenge 
> What does asm0(0xb6,0xc6) return? Submit the flag as a hexadecimal value (starting with '0x')

## Hint
[assembly conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

[basical assembly tutorial](https://www.tutorialspoint.com/assembly_programming/assembly_basic_syntax.htm)
[assembly registers](https://www.tutorialspoint.com/assembly_programming/assembly_registers.htm)

## Solution

	push	ebp
	mov	ebp,esp
	mov	eax,DWORD PTR [ebp+0x8]
	mov	ebx,DWORD PTR [ebp+0xc]
	mov	eax,ebx
	mov	esp,ebp
	pop	ebp	
	ret

---

#### Stack

![https://i.stack.imgur.com/9RelF.png](https://i.stack.imgur.com/9RelF.png)

	Return address is at ebp+0x4
	param1 == 0xb6 is at ebp+0x8
	param2 == 0xc6 is at ebp+0xc

psuedocode

	eax = param1
	ebx = param2
	eax = ebx
	return eax

## Flag

	0xc6