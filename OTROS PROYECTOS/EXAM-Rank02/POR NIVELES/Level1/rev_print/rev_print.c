#include<unistd.h>

void ft_putstr(char *str)
{
    int ind = 0;
    while (str[ind] != 0)
    {
        write (1, &str[ind], 1);
        ind++;
    }
}
int ft_strlen(char *str)
{
    int i = 0;
    while (str[i] != 0)
        i++;
    return (i);
}
#include <stdio.h>
char *ft_reverse(char *str)
{
    int len = ft_strlen(str);
    int ind = 0;
    while (ind <= len/2)
    {
        char temp = str[len-1-ind];
        str[len-1-ind] = str[ind];
        str[ind] = temp;
        ind++;
    }
    return (str);
}

int main(int argc, char** argv)
{
    if(argc != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    char *str = argv[1];
    str = ft_reverse(str);
    ft_putstr(str);
    write(1, "\n", 1);
    return(0);
}