#include <unistd.h>

void ft_putstr(char* str)
{
    int i = 0;
    while(str[i])
    {
        write(1, &str[i], 1);
        i++;
    }
}
void rotone(char* str)
{
    int i = 0;
    while(str[i])
    {
        char c = str[i];
        if(c >= 'a' && c <= 'z')
        {
            c = str[i] + 1;
            if (c > 'z')
                c = 'a';
        }
        else if(c >= 'A' && c <= 'Z')
        {
            c = str[i] + 1;
            if (c > 'Z')
                c = 'A';
        }
        write(1, &c, 1);
        i++;
    }
}

int main(int argc, char** argv)
{
    if (argc != 2)
    {
        write (1, "\n", 1);
        return (0);
    }
    char* msg = argv[1];
    //ft_putstr(msg);
    rotone(msg);
    write (1, "\n", 1);
    return (0);
}
