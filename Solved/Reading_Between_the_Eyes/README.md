# Reading Between the Eyes
Forensics - 150 points

## Challenge 
> Stego-Saurus hid a message for you in [this](husky.png) image, can you retreive it?

## Hint

> Maybe you can find an online decoder?

## Solution

#### Identify the message

Open using StegSolve.

At Red Plane 0, it is completely black except some white pixels in the top left. The same occurs at Green Plane 0, Blue Plane 0.

This means there's some bits hidden in the LSB of each color.

---

The method to extract the message is detailed in this [Stackoverflow post](https://stackoverflow.com/a/22852441)

#### Solve using Python PIL

I refer back to my code from [TPCTF 2017 - Not_Quite_LSD](https://github.com/zst123/tpctf-2017-writeups/tree/master/Solved/Not_Quite_LSD).

Run the script and we get binary

	$ python3 solve.py 
	011100000110100101100011011011110100001101010100010001100111101101110010001100110011010001100100001100010110111001100111010111110110001000110011001101110111011100110011001100110110111001011111001101110110100000110011010111110110001001111001001101110011001101110011011111010000000000000000000000000000

which corresponds to the ascii

picoCTF{r34d1ng_b37w33n_7h3_by73s}

#### Online Solver

Alternatively, there is a convenient online solver.
http://stylesuxx.github.io/steganography/

## Flag

	picoCTF{r34d1ng_b37w33n_7h3_by73s}