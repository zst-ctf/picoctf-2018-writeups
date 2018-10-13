# script me
General Skills - 500 points

## Challenge 
> Can you understand the language and answer the questions to retrieve the flag? Connect to the service with nc 2018shell2.picoctf.com 1542

## Hint
> Maybe try writing a python script?

## Solution

	$ nc 2018shell2.picoctf.com 1542
	Rules:
	() + () = ()()                                      => [combine]
	((())) + () = ((())())                              => [absorb-right]
	() + ((())) = (()(()))                              => [absorb-left]
	(())(()) + () = (())(()())                          => [combined-absorb-right]
	() + (())(()) = (()())(())                          => [combined-absorb-left]
	(())(()) + ((())) = ((())(())(()))                  => [absorb-combined-right]
	((())) + (())(()) = ((())(())(()))                  => [absorb-combined-left]
	() + (()) + ((())) = (()()) + ((())) = ((()())(())) => [left-associative]

	Example: 
	(()) + () = () + (()) = (()())

	Let's start with a warmup.
	(()) + ((())()) = ???

	> ((())(())())
	Correct!

	Okay, now we're cookin!
	((())()) + (()()) + ()() = ???


#### Understanding the rules

Originally I had the following wrong assumptions

1. Comparing `[combine]` and the `[x-absorb-x]` rules, it is absorbed only if the left/right has more than one bracket.
2. From `[left-associative]`, we also do the operation one at a time from left to right

---

However, my first assumption was wrong when trying out and I encountered this from the server.

	((())()) + ((())()) => ((())())((())())

Apparently, the absorb rule only applies if the depth of the brackets are not equal.

For example, wrongly applying absorb-rule to the above will increase the depth and yield the following.

	((())()) depth of 3 +  depth of 3
	Correct answer => ((())())((())()) depth of 3
	Wrong answer => ( ((())()) (())()) depth of 4

With this, I first checked both operands of their depth, and then ***apply absorb-rule only if one is greater than the other*** so that the ***final depth will not change***. For equal depths, the combine rule is used.

#### Translating to code

So I counted the bracket depth of `d1` and `d2` before **inserting the *lower-depth operands* between the brackets** of the higher-depth operands

    d1 = get_total_depth(first)
    d2 = get_total_depth(second)
    
    # [absorb] rule - left is deeper
    if d1 > d2:
        result = first[:-1] + second + first[-1]
    
    # [absorb] rule - right is deeper
    elif d2 > d1:
        result = second[0] + first + second[1:]

    # [combine] rule - equal depth
    else:
        result = first + second

This passes all sample tests assertions

## Flag

	picoCTF{5cr1pt1nG_l1k3_4_pRo_0466cdd7}
