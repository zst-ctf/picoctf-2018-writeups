# assembly-2
Reversing - 250 points

## Challenge 
> What does asm2(0x7,0x28) return? Submit the flag as a hexadecimal value (starting with '0x').

## Hint
> [assembly conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

## Solution

Assembly

	asm2:
		push   	ebp
		mov    	ebp,esp
		sub    	esp,0x10
		mov    	eax,DWORD PTR [ebp+0xc]
		mov 	DWORD PTR [ebp-0x4],eax
		mov    	eax,DWORD PTR [ebp+0x8]
		mov	DWORD PTR [ebp-0x8],eax
		jmp    	part_b
	part_a:	
		add    	DWORD PTR [ebp-0x4],0x1
		add	DWORD PTR [ebp+0x8],0x76
	part_b:	
		cmp    	DWORD PTR [ebp+0x8],0xa1de
		jle    	part_a
		mov    	eax,DWORD PTR [ebp-0x4]
		mov	esp,ebp
		pop	ebp
		ret

Psuedocode

	// => asm2(0x7,0x28)
	// param2 = ebp+0xc == 0x28
	// param1 = ebp+0x8 == 0x07
	// return address = ebp+0x4
	// base pointer = ebp

	asm2:

		byte local1[16] // sub  esp,0x10 ; allocate local param		
		local1[12] = param2 // mov  DWORD PTR [ebp-0x4],eax
		local1[8] = param1 // mov	DWORD PTR [ebp-0x8],eax		
		
		while (param1 <= 0xa1de) {
			local1[12] += 1
			param1 += 0x76
		}
		return local1[12];

So the loop will run `(0xa1de - 0x7) / 0x76` times or 352 times.

So `local1[12]` will increment 352 times to get 0x188

## Flag

	0x188
