void	ft_swap(int *a, int *b)
{
    int temp;

    temp = *a;
    *a = *b;
    *b = temp;
}
/*
#include<stdio.h>
void main()
{
    int a=1, b=3;
    printf("a=%d, b=%d", a, b);
    ft_swap(&a, &b);
    printf("a=%d, b=%d", a, b);
}*/