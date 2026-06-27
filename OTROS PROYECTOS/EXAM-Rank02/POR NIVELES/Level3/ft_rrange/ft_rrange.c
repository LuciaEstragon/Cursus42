//INICIO: 6:37
//FIN: 6:51
//INTENTOS:2

#include <stdlib.h>
int     *ft_rrange(int start, int end)
{
    int *array;
    int i=0;
    int len = end-start;
    array = (int*)malloc(sizeof(int)*len);
    if(!array)
        return (NULL);
    while(i<=len)
    {
        array[i] = end-i;
        i++;
    }
    return(array);
}
/*
#include<stdio.h>
int main()
{
    int* ar=ft_rrange(2,5);
    int i=0;
    int len = 5-2;
    while(i<=len)
    {
        printf("%d", ar[i]);
        i++;
    }
    return 0;
}*/