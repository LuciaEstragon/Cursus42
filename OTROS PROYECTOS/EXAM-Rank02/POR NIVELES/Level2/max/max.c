#include<stdio.h>

int		max(int* tab, unsigned int len)
{
    if(!tab)
        return (0);

    int i = 0;
    int imax = 0;
    while (len != 0)
    {
        if(tab[i] > imax)
            imax = tab[i];
        len--;
        i++;
    }
    return(imax);
}

/*
int main()
{
    int tab[5] = {1, 6, 3, 2, 4};
    unsigned int len = 5;
    printf("%d", max(tab, len));
    return 0;
}*/