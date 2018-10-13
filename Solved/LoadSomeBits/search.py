#! /usr/bin/env python3
##
# Script for PicoCTF Little School Bus challenge
# Created by Amos (LFlare) Ng
##

text_max_length = 600
for iter in range(16):
    with open("pico2018-special-logo.bmp", "rb") as file:
        data = file.read()
        data = data[iter:]

        bits = ""
        for c in data[:text_max_length]:
            lsb = str(c & 0x1)
            bits += lsb

        bytess = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
        lsbstr = "".join(bytess)
        print(iter, lsbstr)
        if "flag" in lsbstr:
            break

