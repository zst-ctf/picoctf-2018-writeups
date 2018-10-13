# roulette
General Skills - 350 points

## Challenge 
> [This Online Roulette Service is in Beta](roulette). Can you find a way to win $1,000,000,000 and get the flag? 

> [Source.](roulette.c) Connect with nc 2018shell2.picoctf.com 48312

## Hint
> There are 2 bugs!


## Solution

#### Bug 1

There is a bug with underflowing the bet money

	How much will you wager?
	Current Balance: $1719 	 Current Wins: 0
	> 4294967295
	Choose a number (1-36)
	> 1

	Spinning the Roulette for a chance to win $4294967294!

	Roulette  :  27

	Nice try..
	Stop wasting your time.

	How much will you wager?
	Current Balance: $1720 	 Current Wins: 0

So we can enter a large number and lose and we will get the money

	Welcome to ONLINE ROULETTE!
	Here, have $3694 to start on the house! You'll lose it all anyways >:)

	How much will you wager?
	Current Balance: $3694 	 Current Wins: 0
	> 3294967295
	Choose a number (1-36)
	> 1

	Spinning the Roulette for a chance to win $2294967294!

	Roulette  :  8 

	Not this time..
	If you keep it up, maybe you'll get the flag in 100000000000 years

	*** Current Balance: $1000003695 ***
	Wait a second... You're not even on a hotstreak! Get out of here cheater!


#### Bug 2

The seed is actually used as the starting money

	long get_rand() {
	  long seed;
	  FILE *f = fopen("/dev/urandom", "r");
	  fread(&seed, sizeof(seed), 1, f);
	  fclose(f);
	  seed = seed % 5000;
	  if (seed < 0) seed = seed * -1;
	  srand(seed);
	  return seed;
	}

	// in main()
	  cash = get_rand();

Hence, we can write a simple program to get our bet numbers.

	./solve-get_spin_value

	Initial value: 2719
	Spin #1: 9
	Spin #2: 36
	Spin #3: 8


----

#### Procedure

- We need to WIN 3 times with bet of $0
- We need to LOSE 1 time with bet of $3294967295 


----

	$ nc 2018shell2.picoctf.com 48312
	Welcome to ONLINE ROULETTE!
	Here, have $2719 to start on the house! You'll lose it all anyways >:)

	How much will you wager?
	Current Balance: $2719 	 Current Wins: 0
	> 0
	Choose a number (1-36)
	> 9

	Spinning the Roulette for a chance to win $0!

	Roulette  :  9 

	You.. win.. this round...

---

	How much will you wager?
	Current Balance: $2719 	 Current Wins: 1
	> 0
	Choose a number (1-36)
	> 36

	Spinning the Roulette for a chance to win $0!

	Roulette  :  36

	Congrats!

---

	How much will you wager?
	Current Balance: $2719 	 Current Wins: 2
	> 0
	Choose a number (1-36)
	> 8

	Spinning the Roulette for a chance to win $0!

	Roulette  :  8 

	You.. win.. this round...

---

	How much will you wager?
	Current Balance: $2719 	 Current Wins: 3
	> 3294967295
	Choose a number (1-36)
	> 1

	Spinning the Roulette for a chance to win $2294967294!

	Roulette  :  21

	Better luck next time...
	Just give up!

	*** Current Balance: $1000002720 ***
	Wow, I can't believe you did it.. You deserve this flag!
	picoCTF{1_h0p3_y0u_f0uNd_b0tH_bUg5_8fb4d984}


## Flag

	picoCTF{1_h0p3_y0u_f0uNd_b0tH_bUg5_8fb4d984}
