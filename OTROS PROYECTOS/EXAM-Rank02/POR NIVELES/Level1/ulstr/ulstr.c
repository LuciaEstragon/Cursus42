#include<unistd.h>

void putstr(char *str)
{
    int i = 0;
    while (str[i] != 0)
    {
        write(1, &str[i], 1);
        i++;
    }
}

char *ulstr(char *str)
{
    int i = 0;
    while (str[i] != 0)
    {
        if(str[i]>=65 && str[i]<=90)
            str[i] += 32;
        else if(str[i]>=97 && str[i]<=122)
            str[i] -= 32;
        i++;
    }
    return (str);
}

int main (int argc, char** argv)
{
    if (argc != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    char* str = argv[1];
    ulstr(str);
    putstr(str);
    write(1, "\n", 1);
    return(0);
}