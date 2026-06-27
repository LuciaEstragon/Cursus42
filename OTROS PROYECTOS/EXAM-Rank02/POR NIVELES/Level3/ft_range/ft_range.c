#include<stdlib.h>
int     *ft_range(int start, int end)
{
    int size = end - start;
    if(size < 0)
        size = -size;
    size ++;
    int *array = (int*)malloc(sizeof(int)*size);
    if(!array)
        return (NULL);
    int i = 0;
    while (size > 0) 
    {
        if(start < end)
        {
            array[i] = start + i;
            i++;
        }
        else
        {
            array[i] = start - i;
            i++;
        }
        size--;
    }
    return (array);
}

/*
#include <stdio.h>
int main()
{
    int *array = ft_range(0, -3);
    int size = 4;
    int i = 0;
    while(size >0)
    {
        printf("%d\n", array[i]);
        size--;
        i++;
    }
    free(array);
    return 0;
}
*/
// -1, 3   -> -1 0 1 2 3 = 5 (3--1)=4+1
// -4, -2  -> -4 -3 -2 = 3  (-2--4)=2+1
// 2, 5    -> 2 3 4 5 = 4  (5-2)=3+1
// 0, -1, -2 -> -2+0 = -2
// 1 0 -1 -2 -> -2-1 = -3