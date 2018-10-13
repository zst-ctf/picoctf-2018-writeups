# buffer overflow 3
Binary Exploitation - 450 points

## Challenge 
> It looks like Dr. Xernon added a stack canary to this [program](vuln) to protect against buffer overflows. 

>Do you think you can bypass the protection and get the flag? You can find it in /problems/buffer-overflow-3_3_6bcc2aa22b2b7a4a7e3ca6b2e1194faf. 

>[Source.](vuln.c)

## Hint
> Maybe there's a smart way to brute-force the canary?


## Solution

- Bruteforce the canary
- Fuzz for the offset size
- Override return address to win()


## Flag

	Progress IHwj
	[+] Starting local process './vuln': pid 1014106
	[*] Switching to interactive mode
	[*] Process './vuln' stopped with exit code -11 (SIGSEGV) (pid 1014106)
	How Many Bytes will You Write Into the Buffer?
	> Input> Ok... Now Where's the Flag?
	picoCTF{eT_tU_bRuT3_F0Rc3_58bc7747}