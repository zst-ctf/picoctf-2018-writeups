# caesar cipher 2
Cryptography - 250 points

## Challenge 
> Can you help us decrypt this [message](ciphertext)? We believe it is a form of a caesar cipher. You can find the ciphertext in /problems/caesar-cipher-2_2_d9c42f8026f320079f3d4fcbaa410615 on the shell server.

## Hint
> You'll have figure out the correct alphabet that was used to encrypt the ciphertext from the ascii character set

>ASCII Table

## Solution

A hard challenge to understand, but simple to solve once I figured it out...
---

Ciphertext

	PICO#4&[C!ESA2?#I0H%R3?JU34?A2%N4?S%C5R%]

From the prefix of picoCTF{, we know that

	P --> p
	# --> C
	4 --> T
	& --> F
	[ --> {

With this, looking at the ASCII table, all the hex codes will be shifted up by 0x20

	$ python3
	>>> ctext = list("PICO#4&[C!ESA2?#I0H%R3?JU34?A2%N4?S%C5R%]")
	>>> ctext = list(map(lambda x: ord(x), ctext))

	>>> text = list(map(lambda x: x + 0x20, ctext))
	>>> ''.join(map(lambda x: chr(x), text))
	'picoCTF{cAesaR_CiPhErS_juST_aREnT_sEcUrE}'


## Flag

	picoCTF{cAesaR_CiPhErS_juST_aREnT_sEcUrE}
