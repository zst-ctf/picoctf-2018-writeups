# Desrouleaux
Forensics - 150 points

## Challenge 
> Our network administrator is having some trouble handling the tickets for all of of our incidents. Can you help him out by answering all the questions? Connect with `nc 2018shell2.picoctf.com 14079`. [incidents.json](incidents.json)

## Hint
> If you need to code, python has some good libraries for it.


## Solution

solve.py

## Flag

	
	$ nc 2018shell2.picoctf.com 14079
	You'll need to consult the file `incidents.json` to answer the following questions.


	What is the most common source IP address? If there is more than one IP address that is the most common, you may give any of the most common ones.
	178.209.2.62
	Correct!


	How many unique destination IP addresses were targeted by the source IP address 178.209.2.62?
	4
	Correct!


	What is the average number of unique destination IP addresses that were sent a file with the same hash? Your answer needs to be correct to 2 decimal places.
	1.67
	Correct!


	Great job. You've earned the flag: picoCTF{J4y_s0n_d3rUUUULo_4f3aae0d}
