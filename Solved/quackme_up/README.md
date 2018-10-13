# quackme up
Reversing - 350 points

## Challenge 
> The duck puns continue. Can you crack, I mean quack this [program](main) as well? You can find the program in /problems/quackme-up_0_740a9bce2dc2d486c687b9d3a6835d73 on the shell server.


## Solution

Notice that the ciphertext is not dependent on the position of the char.

	We're moving along swimmingly. Is this one too fowl for you?
	Enter text to encrypt: a 
	Here's your ciphertext: 00
	Now quack it! : 11 80 20 E0 22 53 72 A1 01 41 55 20 A0 C0 25 E3 20 30 00 45 05 35 40 65 C1
	That's all folks.

	We're moving along swimmingly. Is this one too fowl for you?
	Enter text to encrypt: b
	Here's your ciphertext: 30
	Now quack it! : 11 80 20 E0 22 53 72 A1 01 41 55 20 A0 C0 25 E3 20 30 00 45 05 35 40 65 C1
	That's all folks.

	We're moving along swimmingly. Is this one too fowl for you?
	Enter text to encrypt: abcd
	Here's your ciphertext: 00 30 20 50
	Now quack it! : 11 80 20 E0 22 53 72 A1 01 41 55 20 A0 C0 25 E3 20 30 00 45 05 35 40 65 C1
	That's all folks.

With this, let's just collect the ciphertext of all possible chars, then map it to the quack text

	python solve.py

## Flag

	picoCTF{qu4ckm3_cba512e7}