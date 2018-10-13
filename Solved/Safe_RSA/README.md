# Safe RSA
Cryptography - 250 points

## Challenge 
> Now that you know about RSA can you help us decrypt this [ciphertext](ciphertext)? We don't have the decryption key but something about those values looks funky..

## Solution

N is very big and e is very small, so a cube root can be used.

[Exploit is when n is very big but e is very small](https://github.com/zst123/gryphonctf-2017-writeups/tree/master/Solved/NoWrap)

## Flag

	picoCTF{e_w4y_t00_sm411_7815e4a7}