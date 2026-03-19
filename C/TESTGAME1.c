#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_INPUT 10 //Apparently the number is max characters for the input

int main() {
	char input[MAX_INPUT];

	puts("You see a door. What do you do?\n");
	puts("1. Open");
	puts("2. Knock");
	puts("3. Walk away");

	fgets(input, sizeof(input), stdin);
	//Apparently remove new line
	input[strcspn(input, "\n")] = 0;

	if (strcmp(input, "1") == 0) {
		printf("You open the door, it is just an abandoned house...\n");

	} else if (strcmp(input, "2") == 0) {
		printf("Well...\n");

	} else if (strcmp(input, "3") == 0) {
		printf("Strange noises come from the house....\n");
	}

	return 0;
}
