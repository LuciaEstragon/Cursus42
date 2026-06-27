#include <unistd.h>

void putstr(char* s)
{
    int i = 0;
    while (s[i])
    {
        write(1, &s[i], 1);
        i++;
    }
}

void epur(char* s)
{
    int i = 0;
    int flag = 0;
    int i_alert = 0;
    while (s[i])
        i++;
    int len = i;
    i=0;
    while (i<len)
    {
        while(s[i] == ' ')
        {
            if(i == 0 || s[i+1] == '\0')
            {
                i_alert = 1;
            }
                
            flag = 1;
            i++;
        }
        if(flag == 1 && i_alert != 1)
            write(1, " ", 1);
        if(s[i] != '\0')
        {
            write(1, &s[i], 1);
        }
        i_alert = 0;
        flag = 0;
        i++;
    }
}


int main(int argc, char** argv)
{
    if(argc != 2)
    {
        write(1,"\n",1);
        return 0;
    }
    char *str = argv[1];
    epur(str);
    write(1,"\n",1);
    return 0;
}
