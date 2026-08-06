#include<stdio.h>

int next(int x, int y){
    if(x < 10) {
        printf("x is less than 10");
    } else {
        return -1;
    }
}

int main(){
    int x = 8, y = 20;
    next(x, y);
    return 0;
}