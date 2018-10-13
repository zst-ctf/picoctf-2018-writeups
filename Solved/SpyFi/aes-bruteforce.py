#!/usr/bin/env python3
import socket
import string
import re
from multiprocessing.pool import ThreadPool

charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

def attempt(tag, payload, block_number=0):
    s = socket.socket()
    s.connect(('2018shell2.picoctf.com', 30399))

    # Assert length
    '''
    message = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: """.format(payload)
    assert (len(message) - (block_number + 1) * 16) <= 1, len(message)
    # print(payload)
    '''

    # retrieve char
    while True:
        data = s.recv(4096).decode().strip()
        if not data:
            continue
        #print("Received >>", data)
        
        if 'Welcome, Agent 006!' in data:
            pass
        elif 'Please enter your situation report:' in data:
            s.send(payload.encode())
            s.send(b'\n')
        else:
            return (tag, data[block_number * 32 : block_number * 32 + 32])


def main(progress='', block_number=0):
    # My agent identifying code is: 
    block = 'A' * 16
    assert len(block) == 16

    for skip in range(16):
        # padding to round to nearest block
        # 96 bytes rounded up from 84 bytes provided
        padding = "x" * (96-53-31)
        prefix = padding + block[skip+1:]

        # Enter 15 characters and retrieve the first 16 encoded
        _, aim = attempt('', prefix, block_number)

        pool = ThreadPool(processes=25)
        async_results = []

        # Then enter 16 characters changing the last one until you get the
        # same result as with 15 characters for the first 16 encoded bytes
        for ch in charset:
            # dummy to duplicate the uncontrolled blocks
            # 96 bytes rounded up from 84 bytes provided
            dummy = '\nMy agent identifying code is: '.replace('\n', 'n') # server can't receive newline
            payload = prefix + dummy + progress + ch

            async_result = pool.apply_async(attempt, (ch, payload, block_number))
            async_results.append(async_result)
            
        # That 16th character is the first character of your secret. 
        # You can then repeat the process by putting 14 characters and then
        # finding the second secret characters with the same thechnique.
        for async_result in async_results:
            ch, result = async_result.get()
            print(f"Result: {ch}, {result} == {aim}")

            if result == aim:
                progress += ch
                if ch == '}':
                    # end of flag! if we continue we
                    # merely get '0's added forever
                    print(f"Success! {progress}")
                    quit()
                break

        print(f"Progress (Block {block_number} of index {skip}): {progress}")

    # continue to next block
    main(progress, block_number + 1)

if __name__ == '__main__':
    # 96 bytes rounded up from 84 bytes provided
    # so we mask out the first 6 blocks
    main(block_number=6)