# quackme
Reversing - 200 points

## Challenge 
> Can you deal with the Duck Web? Get us the flag from this [program](main). You can also find the program in /problems/quackme_4_0e48834ea71b521b9f35d29dc7be974e.

## Solution

The flag is given if our payload fulfils `do_magic()`.

Hopper Decompiler

	int do_magic() {
	    var_14 = read_input();
	    var_10 = strlen(var_14);
	    esp = ((esp - 0x10) + 0x10 - 0x10) + 0x10;
	    var_C = malloc(var_10 + 0x1);
	    if (var_C != 0x0) goto loc_8048696;

	loc_804867c:
	    puts("malloc() returned NULL. Out of Memory\n");
	    eax = exit(0xffffffff);
	    return eax;

	.l1:
	    return eax;

	loc_8048696:
	    memset(var_C, 0x0, var_10 + 0x1);
	    esp = (esp - 0x10) + 0x10;
	    var_1C = 0x0;
	    var_18 = 0x0;
	    goto loc_804870b;

	loc_804870b:
	    eax = var_18;
	    if (eax < var_10) goto loc_80486bd;
	    goto .l1;

	loc_80486bd:
	    if ((*(int8_t *)(var_18 + *greetingMessage) & 0xff) == (*(int8_t *)(var_14 + var_18) & 0xff ^ *(int8_t *)(var_18 + 0x8048858) & 0xff)) {
	            var_1C = var_1C + 0x1;
	    }
	    if (var_1C != 0x19) goto loc_8048707;

	loc_80486f5:
	    eax = puts("You are winner!");
	    return eax;

	loc_8048707:
	    var_18 = var_18 + 0x1;
	    goto loc_804870b;
	}

Simplifying


    int do_magic() {
        input_text = read_input();
        input_len = strlen(input_text);
        esp = ((esp - 0x10) + 0x10 - 0x10) + 0x10;
        var_C = malloc(input_len + 0x1);
        if (var_C != 0x0) goto loc_8048696;

        // if fail allocate in malloc
    loc_804867c:
        puts("malloc() returned NULL. Out of Memory\n");
        eax = exit(0xffffffff);
        return eax;

        // if success allocate in malloc
    loc_8048696:
        memset(var_C, 0x0, input_len + 0x1);
        esp = (esp - 0x10) + 0x10;

        // create variables
        count = 0x0;
        index = 0x0;
        goto loc_804870b;

    loc_804870b:
        if (index < input_len) goto loc_80486bd;
        return index;

    loc_80486bd:
        //if ((*(int8_t *)(index + *greetingMessage) & 0xff) == (*(int8_t *)(input_text + index) & 0xff ^ *(int8_t *)(index + 0x8048858) & 0xff)) {
        // 0x8048858 --> sekrutBuffer

        if (greetingMessage[index] == (input_text[index] ^ sekrutBuffer[index]) {
                count++;
        }
        if (count != 25) goto loc_8048707;

    loc_80486f5:
        eax = puts("You are winner!");
        return eax;

    loc_8048707:
        index++;
        goto loc_804870b;
    }

So now we need our input_text payload to be `25` chars of `(greetingMessage[index] ^ sekrutBuffer[index])`

I've extracted sekrutBuffer and then wrote a program to XOR to form our payload.

	$ gcc payload.c -o pay
	$ ./pay
	picoCTF{qu4ckm3_5f8d9c17}

## Flag

	picoCTF{qu4ckm3_5f8d9c17}
