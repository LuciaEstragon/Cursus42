#include<unistd.h>

void putstr(char *str)
{
    int i = 0;

    while (str[i])
    {
        write(1, &str[i], 1);
        i++;
    }
}

void camelsnake(char *str)
{
    int i = 0;

    while (str[i])
    {
        if(i != 0)
        {
            if(str[i]>='A' && str[i]<='Z')
            {
                write(1, "_", 1);
                str[i] += 32;
            }
        }
        write(1, &str[i], 1);
        i++;
    }
}

int main(int argc, char **argv)
{
    if(argc != 2)
    {
        write(1,"\n", 1);
        return (0);
    }
    char *msg = argv[1];
    camelsnake(msg);
    write(1,"\n", 1);
    return (0);

}