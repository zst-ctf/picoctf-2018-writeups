# in out error
General Skills - 275 points

## Challenge 
> Can you utlize stdin, stdout, and stderr to get the flag from [this program](in-out-error)? You can also find it in /problems/in-out-error_4_c51f68457d8543c835331292b7f332d2 on the shell server

## Hint
> Maybe you can split the stdout and stderr output?


## Solution

https://stackoverflow.com/questions/11087499/bash-how-do-you-capture-stderr-to-a-variable

	$ echo 'Please may I have the flag?' > ~/derp.txt
	$ ./in-out-error 2>&1 > /dev/null < ~/derp.txt 
	picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h


## Flag

	picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}
