# HEEEEEEERE'S Johnny
Cryptography - 100 points

## Challenge 
> Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with `nc 2018shell2.picoctf.com 40157`. 

> Files can be found here: [`passwd`](passwd) [`shadow`](shadow).

## Solution

On a Mac, install John the Ripper

	$ brew install john-jumbo

Crack it, it literally took like 1 second

	$ /usr/local/Cellar/john-jumbo/1.8.0/share/john/unshadow ./passwd ./shadow > ./result.db

	$ /usr/local/Cellar/john-jumbo/1.8.0/share/john/john ./result.db 
	Warning: detected hash type "sha512crypt", but the string is also recognized as "sha512crypt-opencl"
	Use the "--format=sha512crypt-opencl" option to force loading these as that type instead
	Warning: hash encoding string length 98, type id $6
	appears to be unsupported on this system; will not load such hashes.
	Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 64/64 OpenSSL])
	Press 'q' or Ctrl-C to abort, almost any other key for status
	kissme           (root)
	1g 0:00:00:03 DONE 2/3 (2018-09-29 11:51) 0.2932g/s 693.5p/s 693.5c/s 693.5C/s kissme
	Use the "--show" option to display all of the cracked passwords reliably
	Session completed

So the password is:

	kissme

View result.db and we know the username is:
	
	root

Login
	
	$ nc 2018shell2.picoctf.com 40157
	Username: root
	Password: kissme
	picoCTF{J0hn_1$_R1pp3d_1b25af80}


## Flag

	??