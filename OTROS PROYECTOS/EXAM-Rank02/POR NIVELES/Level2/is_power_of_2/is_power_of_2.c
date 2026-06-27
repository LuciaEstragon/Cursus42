#include <stdio.h>

int	    is_power_of_2(unsigned int n)
{
    if(n !=1 && n%2 != 0) // si pones esto, cuidadito con el 1
        return(0);//no es potencia de dos
    unsigned int res = 1;
    while (res <= n) //(n >= res)
    {
        if(res == n)
            return(1);//SI es potencia de dos
        res = res*2;
    }
    return(0);//no es potencia de dos
}

/*
int main()
{
    if (is_power_of_2(1))
        printf("%s", "si");
    else
        printf("%s", "no");
    return (0);
}*/