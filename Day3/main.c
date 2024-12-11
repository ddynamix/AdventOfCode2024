/**
 * Author: Tyler Steptoe
 * main.c
 * For AdventOfCode2024 Day3
 * and to study for CSC209 final.
 */

#include <regex.h>
#include <string.h>
#include <stdio.h>

#define INPUT_FILE "input.txt"

regex_t regex;
int reti;
char msgbuf[100];

int main(int argc, char const *argv[]) {
	FILE *fptr;
	fptr = fopen(INPUT_FILE, "r");
	char buff[2000];

	reti = regcomp(&regex, "^mul\\([0-9]{1,3},[0-9]{1,3}\\$", REG_EXTENDED);
	if (reti) {
		fprintf(stderr, "Could not compile regex\n");
		exit(1);
	}

	while(fgets(buff, 2000, fptr)) {
		
	}
}

