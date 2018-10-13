# SpyFi
Cryptography - 300 points

## Challenge 
> James Brahm, James Bond's less-franchised cousin, has left his secure communication with HQ running, but we couldn't find a way to steal his agent identification code. Can you? 

> Conect with nc 2018shell2.picoctf.com 30399. [Source.](spy_terminal_no_flag.py)

## Hint
> What mode is being used?


## Solution
We know that we can control the payload, followed by AES-ECB encryption. Hence, we can do a Chosen Plaintext attack using AES-ECB.

I have done this before in [CSAW CTF 2017 - Babycrypt](https://github.com/zst123/csaw_ctf-2017-writeups/tree/master/baby_crypt)

---

So let's look at the encrypted message

	message = """Agent,
	Greetings. My situation report is as follows:
	{0}
	My agent identifying code is: {1}.
	Down with the Soviets,
	006
	""".format( sitrep, agent_code )

We know that `[53 bytes] + [payload] + [31 bytes] + [flag] + [...]`.

Since 84 bytes are provided by us, let's round it up to the nearest multiple of 16 bytes, which is 96 bytes or 6 blocks.

**This gives us a padding of 12 bytes**

---

A simple AES-ECB attack has the payload on the 0th block and the flag on the 1st block, so in this case we can conduct our attack from the 6th block as the payload and the 7th block as the flag.

So at the start, it should be 7 blocks wide or indexes 0 through 6.

	[53 bytes] + [12 byte: padding] + [16 byte: payload] + [31 bytes]

	Block 3: 'ows:\nxxxxxxxxxxx'
	Block 4: 'xAAAAAAAAAAAAAAA'
	Block 5: 'A\nMy agent ident'
	Block 6: 'ifying code is: '

After which we retrieve the first char of the flag by reducing the payload to 15 bytes.

	[53 bytes] + [12 byte: padding] + [15 byte: payload] + [31 bytes] + [1 byte of flag]

	Block 4: 'xAAAAAAAAAAAAAAA' <-- padding + 15 bytes of the payload
	Block 5: '\nMy agent identi'
	Block 6: 'fying code is: X' <-- X in place of actual flag value

We now store the value of block 6 which has the first char of the flag.

---

Now we need to compare a chosen plaintext to that block 6 saved.

We do this by adding our chosen dummy text which is exactly the same as the server text.

	[53 bytes] + [12 byte: payload] + [15 byte: payload] + [31 byte: chosen dummy] + [31 bytes: actual] + [1 byte of flag]

	Block 4: 'xAAAAAAAAAAAAAAA'
	Block 5: '\nMy agent identi'
	Block 6: 'fying code is: X' <-- our dummy text, were X is iterated through all of charset
	Block 7: '\nMy agent identi' <-- of server, can be ignored
	Block 8: 'fying code is: X' <-- of server, can be ignored

So we can bruteforce for that respective char such that 
	
	[31 byte: chosen dummy] == [31 bytes: actual] + [1 byte of flag] 

---

After a few iterations, it will look similar to this

	Block 4: 'xAAAAAAAAA\nMy ag'
	Block 5: 'ent identifying '
	Block 6: 'code is: picoCTF' <-- The flag is slowly being extracted
	Block 7: '\nMy agent identi' <-- of server, can be ignored
	Block 8: 'fying code is: X' <-- of server, can be ignored


## Flag

	$ python3 aes-bruteforce.py 
	...
	Success! picoCTF{@g3nt6_1$_th3_c00l3$t_8220250}
