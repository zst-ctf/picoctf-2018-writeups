# LoadSomeBits
Forensics - 550 points

## Challenge 
> Can you find the flag encoded inside this image? You can also find the file in /problems/loadsomebits_3_8933ebe9085168b1e0bbb07884c2231f on the shell server.

[pico2018-special-logo.bmp](pico2018-special-logo.bmp)

## Hint
> Look through the Least Significant Bits for the image
If you interpret a binary sequence (seq) as ascii and then try interpreting the same binary sequence from an offset of 1 (seq[1:]) as ascii do you get something similar or completely different?


## Solution

Hint is very direct, and it also reminds me of last year's challenge...

Using the exact same script courtesy of[@LFlare from PicoCTF 2017: Little School Bus](https://github.com/LFlare/picoctf_2017_writeup/tree/master/forensics/little-school-bus), we get the flag.

## Flag

	picoCTF{st0r3d_iN_tH3_l345t_s1gn1f1c4nT_b1t5_449088860}