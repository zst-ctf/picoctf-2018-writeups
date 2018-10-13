# Recovering From the Snap
Forensics - 150 points

## Challenge 
> There used to be a bunch of [animals](animals.dd) here, what did Dr. Xernon do to them?

## Hint
> Some files have been deleted from the disk image, but are they really gone?


## Solution

Foremost can extract deleted files from `.dd`s.

	$ foremost animals.dd 
	Processing: animals.dd
	|*|


## Flag

	00005861.jpg
	
![00005861.jpg](00005861.jpg)