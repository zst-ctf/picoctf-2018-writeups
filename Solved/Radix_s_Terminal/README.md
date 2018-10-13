# Radix's Terminal
Reversing - 400 points

## Challenge 
> Can you find the password to [Radix's login](radix)? You can also find the executable in /problems/radix-s-terminal_1_35b3f86ea999e44d72e988ef4035e872?

## Hint
> https://en.wikipedia.org/wiki/Base64


## Solution

Open in Hopper Decompiler

	int check_password(int arg0) {
	    // lots of code

	    eax = strncmp(var_20, "cGljb0NURntiQXNFXzY0X2VOQ29EaU5nX2lTX0VBc1lfMTg3NTk3NDV9", var_28);
	    ebx = *0x14 ^ *0x14;
	    if (ebx != 0x0) {
	            eax = __stack_chk_fail();
	    }
	    return eax;
	}

Decode using base64

	cGljb0NURntiQXNFXzY0X2VOQ29EaU5nX2lTX0VBc1lfMTg3NTk3NDV9


## Flag

	picoCTF{bAsE_64_eNCoDiNg_iS_EAsY_18759745}