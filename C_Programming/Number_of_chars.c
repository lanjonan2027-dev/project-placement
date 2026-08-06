#include <stdio.h>

int main()
{
    char ch1, ch2;
    int count;

    printf("Enter two characters: ");
    scanf(" %c %c", &ch1, &ch2);

    count = ch2 - ch1 - 1;

    printf("Number of characters between them = %d", count);

    return 0;
}