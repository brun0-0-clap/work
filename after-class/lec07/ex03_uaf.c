#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main() {
    char *greeting = malloc(32);
    strcpy(greeting, "Hello, world!");
    printf("%s\n", greeting);

    greeting[0] = 'J';
    printf("%s\n", greeting);
	free(greeting);
    return 0;
}
