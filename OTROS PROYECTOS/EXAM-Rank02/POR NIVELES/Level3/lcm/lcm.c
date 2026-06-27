#include <stdlib.h>
#include <limits.h>
#include<stdio.h>

unsigned int    hcf_fun(unsigned int a, unsigned int b)
{
    unsigned int hcf = 1;
    unsigned int n = 100000;
    while (n >= 2)
    {
        while(a%n == 0 && b%n == 0)
        {
            hcf = n*hcf;
            a = a/n;
            b = b/n;
        }
        n--;
    }
        return(hcf);
}

/*
while(a%2 == 0 && b%2 == 0)
{
    hcf = 2*hcf;
    a = a/2;
    b = b/2;
}
*/

unsigned int    lcm(unsigned int a, unsigned int b)
{
    unsigned int    hcf = hcf_fun(a, b); 
    unsigned int    L = (a * b)/hcf;
    return (L);
}
/*
int main()
{
    unsigned int a=12, b=16;
    unsigned int  L =  lcm(a,  b);
    printf("%u", L);
    return (0);
}*/