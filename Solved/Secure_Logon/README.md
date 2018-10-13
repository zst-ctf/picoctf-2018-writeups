# Secure Logon
Web Exploitation - 500 points

## Challenge 
> Uh oh, the login page is more secure... I think. http://2018shell2.picoctf.com:56265 (link). Source.

## Hint
> There are versions of AES that really aren't secure.


## Solution

AES CBC is used for the cookie.

The session dict plaintext is shown to us upon login. And the cookie value is the session dict ciphertext with IV.


This is the plaintext

	{'admin': 0, 'password': 'hi', 'username': 'hi'}

I want to modify admin to 1, and the integer happens to reside in the first block.

Hence, it is very easy to just flip one bit of the IV.

Upon flipping the bit and using the new cookie, the website shows us the flag

## Flag

	Flag: picoCTF{fl1p_4ll_th3_bit3_2efa4bf8}
