# learn gdb
General Skills - 300 points

## Challenge 
> Using a debugging tool will be extremely useful on your missions. Can you run this [program](run) in gdb and find the flag? You can find the file in /problems/learn-gdb_3_f1f262d9d48b9ff39efc3bc092ea9d7b on the shell server.

## Hint

	Try setting breakpoints in gdb
	Try and find a point in the program after the flag has been read into memory to break on
	Where is the flag being written in memory?

## Solution

References

- https://ubuntuforums.org/showthread.php?t=989488
- https://stackoverflow.com/questions/10501268/gdb-break-after-function-has-returned
- https://stackoverflow.com/questions/1530736/how-to-print-a-null-terminated-string-with-newlines-without-showing-backslash-es

If we decompile the program, we see that the flag is read into memory when `decrypt_flag()` is executed.

Furthermore, the flag is read into `flag_buf[]`

---

Decrypt the flag

	(gdb) break decrypt_flag
	Breakpoint 1 at 0x40078a
	(gdb) run
	Starting program: /FILES/run 
	Decrypting the Flag into global variable 'flag_buf'

	Breakpoint 1, 0x000000000040078a in decrypt_flag ()
	(gdb) finish
	Run till exit from #0  0x000000000040078a in decrypt_flag ()
	.....................................
	0x000000000040090a in main ()

Now read the flag using print/printf

	(gdb) info add flag_buf         
	Symbol "flag_buf" is at 0x6013e8 in a file compiled without debugging.

	(gdb) print flag_buf
	'flag_buf' has unknown type; cast it to its declared type

	(gdb) print (char*) flag_buf
	$1 = 0x602260 "picoCTF{gDb_iS_sUp3r_u53fuL_efaa2b29}"

	(gdb) printf "%s", (char*) flag_buf
	picoCTF{gDb_iS_sUp3r_u53fuL_efaa2b29}

## Flag

	picoCTF{gDb_iS_sUp3r_u53fuL_efaa2b29}
