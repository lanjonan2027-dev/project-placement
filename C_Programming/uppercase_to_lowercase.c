#program to generate uppercase to lowercase

#include<stdio.h>

int main(){

    char ch;
    printf("Enter a character: ");
    scanf("%c", &ch);

    if(ch >= 'A' && ch <= 'Z'){
        ch = ch + 32;
        printf("Lowercase: %c\n", ch);
    } else {
        printf("The character is not an uppercase letter.\n");
    }

    return 0;
}