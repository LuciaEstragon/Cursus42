#include<unistd.h>
#include<stdio.h>

int MCD(int a, int b)
{
    if(a==1 || b==1)
        return 1;
    
    int ind = 0;
    if (a>b)
        ind = a+1;
    else
        ind =b +1;
    while(1)
    {
        if(a%ind == 0 && b%ind==0)
            return ind;
        ind--;
    }
    return 0;
}
int ft_strlen(char *str)
{
    int len = 0;
    while(str[len])
        len++;
    return (len);
}
int ft_atoi(char* str)
{
    int numb = 0;
    int digit = ft_strlen(str);
    int ind = 0; 
    if(str[ind]<='0' || str[ind]>='9')
        return 0;
    while (ind<digit)
    {
        numb = numb*10 + str[ind] - '0';
        ind++; 
    }
    return (numb);
}
void putnmb(int n)
{
    if(n>=10)
        putnmb(n/10);
    char a = (n%10) + '0';
    write(1, &a, 1);
}

int main(int argc, char **argv)
{
    if (argc!=3)
    {
        write(1, "\n", 1);
        return 0;
    }
    int a = ft_atoi(argv[1]);
    int b = ft_atoi(argv[2]);
    int result = MCD(a, b);
    putnmb(result);
    write(1, "\n", 1);
    return 0;
}