# assembly-4
Reversing - 550 points

## Challenge 
> Can you find the flag using the following assembly source? WARNING: It is VERY long...

## Hint
> Hmm.. There must be an easier way than reversing the whole thing right?

## Solution

### Trying to reverse


References:
 - https://stackoverflow.com/questions/3818755/imul-assembly-instruction-one-operand
 - https://stackoverflow.com/questions/3378543/what-does-push-ebp-mean-in-x86-assemby
 - https://en.wikipedia.org/wiki/Call_stack#Structure
 - https://reverseengineering.stackexchange.com/a/17225
 - https://www.aldeid.com/wiki/X86-assembly/Instructions/lea


There is a series of functions `rrf*` which returns the respective ASCII value of the mentioned char.

---

For add() and sub() methods:

	add:
	        movsx   ecx, byte [esp+4H]   ; ecx = (int8) param1; // copy with sign bit
	        sub     ecx, 48              ; ecx -= 48;
	        add     ecx, dword [esp+8H]  ; ecx += (int32) param2;
	        mov     edx, 3524075731      ; edx = 3524075731;
	        mov     eax, ecx             ; eax = ecx;
	        imul    edx                  ; edx:eax = edx * eax;
	        add     edx, ecx             ; edx += ecx;
	        sar     edx, 6               ; edx >>= 6
	        mov     eax, ecx             ; eax = ecx
	        sar     eax, 31              ; eax >>= 31
	        sub     edx, eax             ; edx -= eax
	        imul    edx, edx, 78         ; edx = edx * 78
	        sub     ecx, edx             ; ecx -= edx
	        lea     eax, [ecx+30H]       ; return [ecx+48]
	        ret


	// Psuedocode
	c = (param1 + param2 - 48)
	edx:eax = 3524075731 * c;
	edx:eax += (c << 32)
	edx >>= 6
	edx -= (c >> 31)
	edx *= 78
	c -= edx
	return x+48

	// Condensed
	c = (param1 + param2 - 48)
	d = (3524075731 * c) >> 32
	d += c
	d >>= 6
	d -= (c >> 31)
	d *= 78
	return c-d+48



#### Compiling

The hint is telling us to compile it

	$ nasm -f elf comp.nasm 
	$ gcc -m32 comp.o -o comp  
	$ ./comp
	picoCTF{1_h0p3_y0u_c0mP1l3d_tH15_94698637933

## Flag

If your flag does not work, EITHER replace the trailing '3's at the end with a '}' OR change '2390040222' to '2350040222' and change '70u' to 'y0u'

	picoCTF{1_h0p3_y0u_c0mP1l3d_tH15_946986379}
