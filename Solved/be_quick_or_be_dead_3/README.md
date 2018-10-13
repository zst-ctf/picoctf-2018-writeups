# be-quick-or-be-dead-3
Reversing - 350 points

## Challenge 
> As the song draws closer to the end, another executable [be-quick-or-be-dead-3](be-quick-or-be-dead-3) suddenly pops up. This one requires even faster machines. Can you run it fast enough too? You can also find the executable in /problems/be-quick-or-be-dead-3_2_fc35b1f6832df902b8e2f724772d012f.


## Hint
> How do you speed up a very repetitive computation?


## Solution

Decompiled code

	void calculate_key() {
	    calc(0x19965);
	    return;
	}

	int calc(int var_24) {
	    if (var_24 <= 0x4) {
	            var_14 = var_24 * var_24 + 0x2345;
	    } else {
	            var_14 = calc(var_24 - 0x5) * 0x1234 + (calc(var_24 - 0x1) - calc(var_24 - 0x2)) + (calc(var_24 - 0x3) - calc(var_24 - 0x4));
	    }
	    return var_14;
	}

	int print_flag() {
	    puts("Printing flag:");
	    decrypt_flag(*(int32_t *)__TMC_END__);
	    rax = puts(0x601080);
	    return rax;
	}

---

Similar to be-quick-or-be-dead-2, the calculate_key() function takes a long time. Unfortunately, it is not a simple algorithm easily found on the internet.

Like the fibonacci function, the calc() function can be sped up using ***memoization***. Python has a [built in memoization decorator](https://www.ynonperek.com/2018/01/11/quick-tip-using-memoization-to-speed-up-recursive-functions/), which is very easy to use.

In a few seconds, we get our result. I printed limited to a 64-bit integer.

	 $ time python3 memoize.py 
	Result: 12083287467950786958

Run in GDB

	(gdb) b main
	Breakpoint 1 at 0x4008aa
	
	(gdb) run
	Starting program: /FILES/be-quick-or-be-dead-3 
	Breakpoint 1, 0x00000000004008aa in main ()
	
	(gdb) call (int) decrypt_flag(12083287467950786958)
	$1 = 41
	
	(gdb) call puts(0x601080) 
	picoCTF{dynamic_pr0gramming_ftw_b5c45645}
	$2 = 42
	

## Flag

	picoCTF{dynamic_pr0gramming_ftw_b5c45645}
