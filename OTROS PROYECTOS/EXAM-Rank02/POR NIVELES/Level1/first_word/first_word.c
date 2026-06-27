#include <stdio.h>
#include <unistd.h>

void ft_putstr(char *str)
{
    int i = 0;
    while(str[i] != 0)
    {
        write(1, &str[i], 1);
        i++;
    }
}
char *first_word(char *str)
{
    int i = 0;
    char *ptr;
    int flag = 0;
    while(str[i] != 0)
    {
        if(str[i] != ' ' && flag == 0)
        {
            int j = 0;
            while(str[i] != ' ' || j<=10)
            {
                ptr[j] = str[i];
                j++;
                i++;
            }
            printf("%s\n\n\n", ptr);
            flag = 1;
            ptr[j]='\0';
            i++;
        }
        i++;
    }
    return (ptr);
}
int main (int argc, char **argv)
{
    if(argc != 2)
    {
        write(1, "\n", 1);
        return(0);
    }
    char *str = argv[1];
    ft_putstr(str);
    str = first_word(str);
    ft_putstr(str);
    write(1, "\n", 1);
    return(0);
}
