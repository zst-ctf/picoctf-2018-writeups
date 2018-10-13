# Artisinal Handcrafted HTTP 3
Web Exploitation - 300 points

## Challenge 
> We found a hidden flag server hiding behind a proxy, but the proxy has some... _interesting_ ideas of what qualifies someone to make HTTP requests. Looks like you'll have to do this one by hand. Try connecting via nc 2018shell2.picoctf.com 2651, and use the proxy to send HTTP requests to `flag.local`. We've also recovered a username and a password for you to use on the login page: `realbusinessuser`/`potoooooooo`.


## Hint
> _Be the browser._ When you navigate to a page, how does your browser send HTTP requests? How does this change when you submit a form?

## Solution

We basically need to manually create HTTP GET and POST requests.

- http://www.ntu.edu.sg/home/ehchua/programming/webprogramming/http_basics.html

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies

See [log.txt](log.txt)

## Flag

	picoCTF{0nLY_Us3_n0N_GmO_xF3r_pR0tOcol5_5f5f}
