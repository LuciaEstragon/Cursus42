#include <unistd.h>

void put_str(char *str)
{
    int i = 0;
    
    while (str[i] != 0)
    {
        write (1, &str[i], 1);
        i++;
    }
}

void rot_13(char *str)
{
    int i = 0;
    
    while (str[i] != 0)
    {
        if(str[i] >= 65 && str[i] <= 90)
        {
            str[i] += 13;
            if(str[i] > 90)
            {
                int diff = str[i] -90;
                str[i] = 65+diff-1;
            }
        }
        else if (str[i] >= 97 && str[i] <= 122)
        {
            if(str[i] >= 110)
            {
                str[i] = str[i]-26+13;
            }
            else
                str[i] += 13;

        }
        write (1, &str[i], 1);
        i++;
    }
}

int main(int c, char** arg)
{
    if (c != 2)
    {
        write (1, "\n", 1);
        return (0);
    }
    char *msg = arg[1];
    ///put_str(msg);
    rot_13(msg);
    write (1, "\n", 1);
    return (0);
}