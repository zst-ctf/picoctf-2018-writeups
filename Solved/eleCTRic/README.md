# eleCTRic
Cryptography - 400 points

## Challenge 
> You came across a custom server that Dr Xernon's company eleCTRic Ltd uses. It seems to be storing some encrypted files. Can you get us the flag? Connect with nc 2018shell2.picoctf.com 42185. [Source.](eleCTRic.py)

## Hint
> I have repeated myself many many many times- do not repeat yourself.

> Do I need to say it in different words? You mustn't repeat thyself.

## Solution

### Theory of CTR mode

![aes-ctr.png](aes-ctr.png)

https://crypto.stackexchange.com/questions/33846/is-regular-ctr-mode-vulnerable-to-any-attacks

https://crypto.stackexchange.com/questions/48397/brute-force-get-aes-keys-by-multiple-plain-texts-with-their-cipher-texts
	
	With CTR or OFB mode, this is trivial: XORing any ciphertext with the corresponding plaintext will give you the keystream, which you can then XOR with any other ciphertext to decrypt it. Or, if you're feeling lazy, just take any ciphertext and submit it as the plaintext for encryption. Since CTR and OFB mode encryption and decryption are the same operation, this will directly give you the original decrypted message.

We have control over the input (filename when creating a new file) and the output (the share code generated from the filename is given to us).

Since in AES-CTR mode, the keystream is kept constant, we can do `plaintext XOR ciphertext = keystream`. Or in context of the problem it will be `filename.txt XOR share_code1 = keystream`

After which, we can do `flag_filename.txt ^ keystream = share_code2`.

We then submit `share_code2` to the server to get the flag.

### Solving
	
	$ nc 2018shell2.picoctf.com 42185
	Initializing Problem...
	Welcome to eleCTRic Ltd's Safe Crypto Storage
	---------------------------------------------

	Choices:
	  E[n]crypt and store file
	  D[e]crypt file
	  L[i]st files
	  E[x]it
	Please choose: n   

	Name of file? AAAAAAAAAAAAAAAAAAAAAAAAA
	Data? AAAAAAAAAAAAAAAAAAAAAAAAA
	Share code:
	aDRAiN4cUN+kAiCJOlEo+mg0QIjeHFDfpG0VsA8=

	Choices:
	  E[n]crypt and store file
	  D[e]crypt file
	  L[i]st files
	  E[x]it
	Please choose: i

	Files:
	  AAAAAAAAAAAAAAAAAAAAAAAAA.txt
	  flag_e734862f2a5dffdcd8c8.txt

	Choices:
	  E[n]crypt and store file
	  D[e]crypt file
	  L[i]st files
	  E[x]it
	Please choose: e

	Share code? TxlgrsA4Jq3Re1f6HSIIjk0TZ638OSn93W0VsA8=
	Data: 
	picoCTF{alw4ys_4lways_Always_check_int3grity_6ce3f91c}

	Choices:
	  E[n]crypt and store file
	  D[e]crypt file
	  L[i]st files
	  E[x]it
	Please choose: 


## Flag

	picoCTF{alw4ys_4lways_Always_check_int3grity_6ce3f91c}
