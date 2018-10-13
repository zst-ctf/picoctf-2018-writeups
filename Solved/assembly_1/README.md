# assembly-1
Reversing - 200 points

## Challenge 
> What does asm1(0x76) return? Submit the flag as a hexadecimal value (starting with '0x'). 

## Hint
[assembly conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

## Solution

Assembly

	asm1:
		push	ebp
		mov	ebp,esp
		cmp	DWORD PTR [ebp+0x8],0x98
		jg 	part_a	
		cmp	DWORD PTR [ebp+0x8],0x8
		jne	part_b
		mov	eax,DWORD PTR [ebp+0x8]
		add	eax,0x3
		jmp	part_d
	part_a:
		cmp	DWORD PTR [ebp+0x8],0x16
		jne	part_c
		mov	eax,DWORD PTR [ebp+0x8]
		sub	eax,0x3
		jmp	part_d
	part_b:
		mov	eax,DWORD PTR [ebp+0x8]
		sub	eax,0x3
		jmp	part_d
		cmp	DWORD PTR [ebp+0x8],0xbc
		jne	part_c
		mov	eax,DWORD PTR [ebp+0x8]
		sub	eax,0x3
		jmp	part_d
	part_c:
		mov	eax,DWORD PTR [ebp+0x8]
		add	eax,0x3
	part_d:
		pop	ebp
		ret


Psuedocode

	// Return address is at ebp+0x4
	// param1 == 0x76 is at ebp+0x8

	asm1:
		if (param1 > 0x98) {
			goto part_a
		}
		if (param1 != 0x98) {
			goto part_b
		}
		eax = *param1
		eax += 3
		goto part_d

	part_a:
		if (param1 != 0x16) {
			goto part_c
		}
		eax = *param1
		eax -= 3
		goto part_d

	part_b:
		eax = *param1
		eax -= 3
		goto part_d

		// unreachable
		if (param1 != 0xbc) {
			goto part_c
		}
		eax = *param1
		eax -= 3
		goto part_d

	part_c:
		eax = *param1
		eax += 3

	part_d:
		return value;

Psuedocode condensed


	// Return address is at ebp+0x4
	// param1 == 0x76 is at ebp+0x8

	function asm1(param1) {
		if (param1 > 0x98) {
			if (param1 != 0x16) {
				param1 += 3
				return param1
			}
			param1 -= 3
			return param1
		}
		if (param1 != 0x98) {
			param1 -= 3
			return param1
			// unreachable code here
		}
		param1 += 3
		return param1
	}
	asm1(0x76);

---

Since 0x76 != 0x98,

	0x76-0x3 is returned

## Flag

	0x73