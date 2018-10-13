/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define MAX_NUM_LEN 12
#define HOTSTREAK 3
#define MAX_WINS 16
#define ONE_BILLION 1000000000
#define ROULETTE_SIZE 36
#define ROULETTE_SPINS 128
#define ROULETTE_SLOWS 16
#define NUM_WIN_MSGS 10
#define NUM_LOSE_MSGS 5

int main()
{
    // get seed
    long seed;
    printf("Initial value: ");
    scanf("%d", &seed);
    srand(seed);
    
    for (int numb = 1; numb < 4; numb++) {
        // do spin rand()
        long spin = (rand() % ROULETTE_SIZE)+1;
        printf("Spin #%d: %d\n", numb, spin);
        
        // dummy rand() for win message
        long dummy = rand();
    }
    

    return 0;
}
