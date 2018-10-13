# be-quick-or-be-dead-2
Reversing - 275 points

## Challenge 
> As you enjoy this music even more, another executable [be-quick-or-be-dead-2](be-quick-or-be-dead-2) shows up. Can you run this fast enough too? You can also find the executable in /problems/be-quick-or-be-dead-2_0_04f4c579185361da6918bbc2fc9dcb7b.


## Hint
> Can you call stuff without executing the entire program?
What will the key finally be?

## Solution

Decompiled code

	int main(int arg0, int arg1) {
	    header();
	    set_timer();
	    get_key();
	    print_flag();
	    return 0x0;
	}

	int print_flag() {
	    puts("Printing flag:");
	    decrypt_flag(*(int32_t *)__TMC_END__);
	    rax = puts(0x601080);
	    return rax;
	}

	void calculate_key() {
	    fib(0x3f7);
	    return;
	}

---

In the function `void calculate_key()`, the fibbonacci number of `0x3f7` or decimal `1015` is being calculated to be the key.

The fibbonacci number is being calculated in a **very inefficient way**. Using programs that implement memoization, the result will be almost instant

	$ wget https://gist.githubusercontent.com/juniskane/0968c66aec75bee27736d7a2819db141/raw/8550dc13342b73cde732c34506b2a84451ebe360/fib.py

	$ python fib.py 1015
	59288416551943338727574080408572281287377451615227988184724603969919549034666922046325034891393072356252090591628758887874047734579886068667306295291967872198822088710569576575629665781687543564318377549435421485

Now, we can use GDB to call the functions directly without running the entire program.

	(gdb) b main
	Breakpoint 1 at 0x400863

	(gdb) run
	Starting program: /FILES/be-quick-or-be-dead-2 
	Breakpoint 1, 0x0000000000400863 in main ()

	(gdb) call decrypt_flag(59288416551943338727574080408572281287377451615227988184724603969919549034666922046325034891393072356252090591628758887874047734579886068667306295291967872198822088710569576575629665781687543564318377549435421485)
	Numeric constant too large.

Here, the number is too large and we need to have the param as a long integer or 64-bit integer. 

We can scale it by getting the first 64 bits.

	>>> result = 59288416551943338727574080408572281287377451615227988184724603969919549034666922046325034891393072356252090591628758887874047734579886068667306295291967872198822088710569576575629665781687543564318377549435421485
	>>> result & (2**64 - 1)
	17662975587330736941

Now we can decrypt it
	
	(gdb) call (int) decrypt_flag(17662975587330736941)
	$1 = 57

	(gdb) call puts(0x601080)
	picoCTF{the_fibonacci_sequence_can_be_done_fast_73e2451e}
	$2 = 58

## Flag

	picoCTF{the_fibonacci_sequence_can_be_done_fast_73e2451e}
