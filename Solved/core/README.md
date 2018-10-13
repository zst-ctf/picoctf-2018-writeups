# core
Forensics - 350 points

## Challenge 
> This [program](print_flag) was about to print the flag when it died. Maybe the flag is still in this [core](core) file that it dumped? Also available at /problems/core_3_bbdfe8f633bce938028c1339013a4865 on the shell server.

## Hint
> What is a core file?

> You may find this reference helpful.
http://darkdust.net/files/GDB%20Cheat%20Sheet.pdf

> Try to figure out where the flag was read into memory using the disassembly and strace.
https://linux.die.net/man/1/strace

>You should study the format options on the cheat sheet and use the examine (x) or print (p) commands. disas may also be useful.

## Solution

[Decompiling the program](print_flag-decompiled.c), we see that:

1. it reads a seed from the environment variable `SEED_ENV`
2. it reads 32 bytes from the file `./flag`
3. the flag is printed out in the function `print_flag()`
Using GDB we can analyse the memory.

But first let's do a test.

	$ export SEED_ENV="ABCD"
	$ pwn cyclic 32 > flag
	$ ./print_flag 
	your flag is: picoCTF{aaaabaaacaaadaaaeaaafaaagaaahaaa}

In GDB, set a breakpoint and start the program

	$ gdb ./print_flag 

	(gdb) br print_flag
	Breakpoint 1 at 0x80487c7: file ./print_flag.c, line 91.
	
	(gdb) run 
	Starting program: /home/zst123/pr/print_flag 

	Breakpoint 1, print_flag () at ./print_flag.c:91
	91	./print_flag.c: Permission denied.

Now we can analyse the memory

	(gdb) info proc map
	process 2737150
	Mapped address spaces:

		Start Addr   End Addr       Size     Offset objfile
		 0x8048000  0x8049000     0x1000        0x0 /home/zst123/pr/print_flag
		 0x8049000  0x804a000     0x1000        0x0 /home/zst123/pr/print_flag
		 0x804a000  0x804b000     0x1000     0x1000 /home/zst123/pr/print_flag
		 0x804b000  0x80b7000    0x6c000        0x0 [heap]
		0xf7e15000 0xf7e16000     0x1000        0x0 
		...

We can search the stack and heap memory for our flag

	(gdb) find 0x8048000,0x80b7000,"aaaabaaacaaadaaaeaaafaaagaaahaaa"
	0x80610f0
	warning: Unable to access 15984 bytes of target memory at 0x80b3191, halting search.
	1 pattern found.

	(gdb) printf "%s\n", 0x80610f0
	aaaabaaacaaadaaaeaaafaaagaaahaaa

Sweet, our flag is at the address `0x80610f0`...

Now open the core dump file and do the same

	$ gdb ./print_flag ./core 

	Core was generated by `/opt/hacksports/staging/core_3_7696529112109598/problem_files/print_flag'.
	Program terminated with signal SIGTRAP, Trace/breakpoint trap.
	#0  print_flag () at ./print_flag.c:90
	90	./print_flag.c: Permission denied.
	(gdb) printf "%s\n", 0x80610f0
	8a1f03cbcf407a296fa0bcf149fc5879
	(gdb) 

Flag will be printed as `picoCTF{%s}`

## Flag

	picoCTF{8a1f03cbcf407a296fa0bcf149fc5879}