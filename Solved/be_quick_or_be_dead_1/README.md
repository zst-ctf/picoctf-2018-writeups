# be-quick-or-be-dead-1
Reversing - 200 points

## Challenge 
> You find [this](https://www.youtube.com/watch?v=CTt1vk9nM9c) when searching for some music, which leads you to [be-quick-or-be-dead-1](be-quick-or-be-dead-1). Can you run it fast enough? You can also find the executable in /problems/be-quick-or-be-dead-1_4_98374389c5652d0b16055427532f098f.

## Hint
> 


## Solution

Hopper decompiler

	int main(int arg0, int arg1) {
	    header();
	    set_timer();
	    get_key();
	    print_flag();
	    return 0x0;
	}


Call the function directly in GDB

	$ gdb be-quick-or-be-dead-1 

	(gdb) break main
	Breakpoint 1 at 0x40082b

	(gdb) run
	Starting program: /problems/be-quick-or-be-dead-1_4_98374389c5652d0b16055427532f098f/be-quick-or-be-dead-1 

	Breakpoint 1, 0x000000000040082b in main ()

	(gdb) call get_key()
	Calculating key...
	Done calculating key
	$1 = 21
	
	(gdb) call print_flag()
	Printing flag:
	picoCTF{why_bother_doing_unnecessary_computation_402ca676}
	$2 = 59


## Flag

	picoCTF{why_bother_doing_unnecessary_computation_402ca676}
