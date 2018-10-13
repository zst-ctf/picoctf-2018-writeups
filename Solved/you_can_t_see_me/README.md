# you can't see me
General Skills - 200 points

## Challenge 
> '...reading transmission... Y.O.U. .C.A.N.'.T. .S.E.E. .M.E. ...transmission ended...' Maybe something lies in /problems/you-can-t-see-me_0_8fc4b46df0f4dd36b87a28877fcf9ea2.

## Solution

An interesting problem.

We notice a file with dot as the name.

	$ ls -la
	total 60
	drwxr-xr-x   2 root       root        4096 Sep 28 08:34 .
	-rw-rw-r--   1 hacksports hacksports    57 Sep 28 08:34 .  
	drwxr-x--x 576 root       root       53248 Sep 30 03:50 ..

But we can't cat it.

	zst123@pico-2018-shell-2:/problems/you-can-t-see-me_0_8fc4b46df0f4dd36b87a28877fcf9ea2$ cat .
	cat: .: Is a directory
	zst123@pico-2018-shell-2:/problems/you-can-t-see-me_0_8fc4b46df0f4dd36b87a28877fcf9ea2$ cat *
	cat: '*': No such file or directory

However notice that there are 2 spaces after the dot

	zst123@pico-2018-shell-2:/problems/you-can-t-see-me_0_8fc4b46df0f4dd36b87a28877fcf9ea2$ cat '.  '
	picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_e3d80588}
