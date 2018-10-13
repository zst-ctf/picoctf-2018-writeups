# Super Safe RSA
Cryptography - 350 points

## Challenge 
> Dr. Xernon made the mistake of rolling his own crypto.. Can you find the bug and decrypt the message? Connect with nc 2018shell2.picoctf.com 3609.


## Hint
> Just try the first thing that comes to mind.


## Solution

Try out the server

	~ $ nc 2018shell2.picoctf.com 3609
	c: 19186016582318064428291303425902140901883296951420146438700416985707104860040269
	n: 22104805049219253595688155381445306328126758057554593510365000451311355387636863
	e: 65537

I tried all other attacks and it didn't work so I figured out that the solution was to factorise it.

### Factorising using YAFU

	# git clone https://github.com/tamnil/yafu-prime-sieve
	# cd yafu-prime-sieve/
	# ./yafu

	10/07/18 05:51:29 v1.34.5 @ zst_ctf, System/Build Info: 
	Using GMP-ECM 6.4.4, Powered by GMP 5.1.1
	detected Intel(R) Core(TM) i5-7267U CPU @ 3.10GHz
	detected L1 = 32768 bytes, L2 = 4194304 bytes, CL = 64 bytes
	measured cpu frequency ~= 3092.435630
	using 20 random witnesses for Rabin-Miller PRP checks

	===============================================================
	======= Welcome to YAFU (Yet Another Factoring Utility) =======
	=======             bbuhrow@gmail.com                   =======
	=======     Type help at any time, or quit to quit      =======
	===============================================================
	cached 78498 primes. pmax = 999983


	>> factor(22104805049219253595688155381445306328126758057554593510365000451311355387636863)

	fac: factoring 22104805049219253595688155381445306328126758057554593510365000451311355387636863
	fac: using pretesting plan: normal
	fac: no tune info: using qs/gnfs crossover of 95 digits
	div: primes less than 10000
	rho: x^2 + 3, starting 1000 iterations on C80 
	rho: x^2 + 2, starting 1000 iterations on C80 
	rho: x^2 + 1, starting 1000 iterations on C80 
	pm1: starting B1 = 150K, B2 = gmp-ecm default on C80
	ecm: 30/30 curves on C80, B1=2K, B2=gmp-ecm default
	ecm: 74/74 curves on C80, B1=11K, B2=gmp-ecm default
	ecm: 188/188 curves on C80, B1=50K, B2=gmp-ecm default, ETA: 0 sec 

	starting SIQS on c80: 22104805049219253595688155381445306328126758057554593510365000451311355387636863

	==== sieving in progress (1 thread):   46016 relations needed ====
	====           Press ctrl-c to abort and save state           ====
	46091 rels found: 23638 full + 22453 from 238596 partial, (1545.39 rels/sec)

	SIQS elapsed time = 171.6340 seconds.
	Total factoring time = 190.5530 seconds


	***factors found***

	P39 = 144258603536574599963220429490269382037
	P42 = 153230410577313765737534565937792115989699

	ans = 1

Now plug the `p` and `q` values into any typical RSA script and decrypt the ciphertext


## Flag

	$ python3 solve.py 
	picoCTF{us3_l@rg3r_pr1m3$_1335}
