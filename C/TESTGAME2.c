#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//Required libraries to make the program work
//stdio.h allows the standard input / output abilities
//stdlib allows the standard librarby [?]
//string.h allows string handling


#define MAX_INPUT 10 //change number if needed
//defines the max letter uput



int main() {
    char input[MAX_INPUT];

    puts("You see a door. What do you do?\n");
    puts("1. Open");
    puts("2. Knock");
    puts("3. Walk away");

    printf("[INPUT] ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0;

    if (strcmp(input, "1") == 0) {
        printf("You open the door, it is just an abandoned house...\n");

        // --- Nested choice ---
        puts("\nInside, you see a staircase. What now?");
        puts("1. Go upstairs");
        puts("2. Leave");

	printf("[INPUT] ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = 0;

        if (strcmp(input, "1") == 0) {
            printf("You walk upstairs...\n");

        } else if (strcmp(input, "2") == 0) {
            printf("You decide to leave the house.\n");

        } else {
            printf("Invalid choice.\n");
        }

    } else if (strcmp(input, "2") == 0) {
        printf("Well...\n");

    } else if (strcmp(input, "3") == 0) {
        printf("Strange noises come from the house....\n");

    } else {
        printf("Invalid choice.\n");
    }

    return 0;
}
