# Magic Padding Oracle
Cryptography - 450 points

## Challenge 
> Can you help us retreive the flag from this crypto service? Connect with nc 2018shell2.picoctf.com 6246. We were able to recover some [Source Code.](pkcs7.py)

## Hint
> Paddding Oracle Attack

> https://blog.skullsecurity.org/2013/padding-oracle-attacks-in-depth

## Solution

### padding oracle attack

This is a very good article on padding oracle attack

- https://robertheaton.com/2013/07/29/padding-oracle-attack/


In essence, I extract each block I want to attack, then bruteforce for each character using the method in the article.

---

So after extracting, I have all the block values

	$ ./solve-extract.py

	Block 0 - #16: b'\x16\xf7\xb0m\xb94vpd\x1a\xbf\xf3\xdf\xd1\xff\x8a' True
	Solved C0: b'This is an IV456'
	Solved I0: b'\x16\xf7\xb0m\xb94vpd\x1a\xbf\xf3\xdf\xd1\xff\x8a'
	Solved P0: b''

	Block 1 - #16: b'/J\x1c\x00E\x1b\x1dA\x0c\x0b\x02sv\x16RC' True
	Solved C1: b'\xba\xdeY\x10\x97d\xfe\xbe\xa2\xc7u\nM\xae\x94\xdc'
	Solved I1: b'/J\x1c\x00E\x1b\x1dA\x0c\x0b\x02sv\x16RC'
	Solved P1: b'{"username": "gu'

	Block 2 - #16: b'\xdf\xad-2\xbbD\xdc\xdb\xda\xb7\x1cx(\xdd\xb6\xe6' True
	Solved C2: b'\x9dIJ\xfe}/oe\xfb\x13\x96y\x15\x85\xbc\x03'
	Solved I2: b'\xdf\xad-2\xbbD\xdc\xdb\xda\xb7\x1cx(\xdd\xb6\xe6'
	Solved P2: b'est", "expires":'
	
	Block 3 - #16: b'\xbdkx\xceM\x1fBU\xca>\xa6N7\xa9\x9c!' True
	Solved C3: b'\x00\x12u\xdb=]\xc7fj9\xa5\xb1\x15\x9e&\x1a'
	Solved I3: b'\xbdkx\xceM\x1fBU\xca>\xa6N7\xa9\x9c!'
	Solved P3: b' "2000-01-07", "'

	Block 4 - #16: b'ia*\xbaY0\xae\x08H\x03\x85\x93s\xffJi' True
	Solved C4: b'{\xceM\xd13\xa7|\x97\\\xbb\xa1\xdd\xb3u\x1b\xc6'
	Solved I4: b'ia*\xbaY0\xae\x08H\x03\x85\x93s\xffJi'
	Solved P4: b'is_admin": "fals'

	Block 5 - #16: b'\x1e\xec0\xdc>\xaaq\x9aQ\xb6\xac\xd0\xbex\x16\xcb' True
	Solved C5: b'\x9f\x88\xeb\xbf\x9d,\xa5\x9c\xda(#\x0e\xdd\xb2>\x16'
	Solved I5: b'\x1e\xec0\xdc>\xaaq\x9aQ\xb6\xac\xd0\xbex\x16\xcb'
	Solved P5: b'e"}\r\r\r\r\r\r\r\r\r\r\r\r\r'

---


### cbc bit flipping attack

- https://masterpessimistaa.wordpress.com/2017/05/03/cbc-bit-flipping-attack/

We have control over the ciphertext.

We know the formula:

	Pn = C[n-1] ^ In

So let's say I want to modify P5 to change the expiry date, I modify the ciphertext of the previous block... With this, we can slowly modify the blocks starting from the back.

	P5 = C4 ^ I5

- https://crypto.stackexchange.com/a/50050

### Garbled plaintexts after modification

However, when we modify the previous ciphertext, **it also garbles the previous plaintext**. 

***This means that after we modify P5, and change C4, we will affect I4 and in turn P4.*** 


Upon doing each modification, run the extraction process again in order to get our ***new Ix and Px values which have change***.


	$ python3 solve_bitflip.py 
	Original
	b'{"username": "guest", "expires": "2000-01-07", "is_admin": "false"}\r\r\r\r\r\r\r\r\r\r\r\r\r'
	b'This is an IV456\xba\xdeY\x10\x97d\xfe\xbe\xa2\xc7u\nM\xae\x94\xdc\x9dIJ\xfe}/oe\xfb\x13\x96y\x15\x85\xbc\x03\x00\x12u\xdb=]\xc7fj9\xa5\xb1\x15\x9e&\x1a{\xceM\xd13\xa7|\x97\\\xbb\xa1\xdd\xb3u\x1b\xc6\x9f\x88\xeb\xbf\x9d,\xa5\x9c\xda(#\x0e\xdd\xb2>\x16'
	b'5468697320697320616e204956343536bade59109764febea2c7750a4dae94dc9d494afe7d2f6f65fb1396791585bc03001275db3d5dc7666a39a5b1159e261a7bce4dd133a77c975cbba1ddb3751bc69f88ebbf9d2ca59cda28230eddb23e16'

	Bit Flip Block 4
	Block 3 - #16: b'&qVq\x80\x8f\xd0\xe1p\xe0[\xa0\xb6k(\x1e' True
	Solved C3: b'\x00\x12u\xdb=]\xc7fj9\xa5\xb3Q\x8b8\x1c'
	Solved I3: b'&qVq\x80\x8f\xd0\xe1p\xe0[\xa0\xb6k(\x1e'
	Solved P3: b'\xbb8\x1c\x8f\xfd\xa0\xbf\x84\x8b\xf3\xcd\xd9\xa3\xee\x94\x1d'

	Bit Flip Block 3
	Block 2 - #16: b'=\xf5\\u.3\xd9C\x10\xfd\x13\xf5\xb5K\x13\xd9' True
	Solved C2: b'\x06SdA\xb4\xbf\xfd\xd1A\xcdk\x97\x94G\x08<'
	Solved I2: b'=\xf5\\u.3\xd9C\x10\xfd\x13\xf5\xb5K\x13\xd9'
	Solved P2: b"\x87+\x05e\xb9W'\xfd\xb2:f\xff\xf8\xe5\x87\x05"

	Bit Flip Block 2
	Block 1 - #16: b'\x92ym*\xfd`\xcc\xf4\xe3@\xab\x8c/\xa5C\xe8' True
	Solved C1: b'K\x86(W\x02\x13\xfb&h\x8dz\x87\xd081\xe3'
	Solved I1: b'\x92ym*\xfd`\xcc\xf4\xe3@\xab\x8c/\xa5C\xe8'
	Solved P1: b'\xc6\x11\x04Y\xdd\t\xbf\xd4\x82.\x8b\xc5y\x91v\xde'

	Bit Flip Block 1
	Block 0 - #16: b'(y:\xad\x006\xc1\xe9\x9d\xf1\x11\x80\xfc\xd4*\xeb' True
	Solved C0: b'\xe9[\x18Y\x98\x12\xa2\x95\x8e%\x89\xb6\x0f\x87"\x8c'
	Solved I0: b'(y:\xad\x006\xc1\xe9\x9d\xf1\x11\x80\xfc\xd4*\xeb'
	Solved P0: b''

	Final Payload
	b'{"username": "advst", "expires": "2040-01-07", "is_admin":  "true"}\r\r\r\r\r\r\r\r\r\r\r\r\r'
	b'e95b18599812a2958e2589b60f87228c4b8628570213fb26688d7a87d03831e306536441b4bffdd141cd6b979447083c001275db3d5dc7666a39a5b3518b381c7bce4dd133a77c975cbba1ddb3751bc69f88ebbf9d2ca59cda28230eddb23e16'
	Magic_Padding_Oracle $ 

And by doing so, we get a valid ciphertext

	$ nc 2018shell2.picoctf.com 6246

	Welcome to Secure Encryption Service version 1.65

	Here is a sample cookie: 5468697320697320616e204956343536bade59109764febea2c7750a4dae94dc9d494afe7d2f6f65fb1396791585bc03001275db3d5dc7666a39a5b1159e261a7bce4dd133a77c975cbba1ddb3751bc69f88ebbf9d2ca59cda28230eddb23e16
	What is your cookie?
	e95b18599812a2958e2589b60f87228c4b8628570213fb26688d7a87d03831e306536441b4bffdd141cd6b979447083c001275db3d5dc7666a39a5b3518b381c7bce4dd133a77c975cbba1ddb3751bc69f88ebbf9d2ca59cda28230eddb23e16
	username: advst
	Admin? true
	Cookie is not expired
	The flag is: picoCTF{0r4cl3s_c4n_l34k_86bb783e}

## Flag

	picoCTF{0r4cl3s_c4n_l34k_86bb783e}
