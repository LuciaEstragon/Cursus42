#include <unistd.h>

void putstr(char *s)
{
    int i = 0;
    while (s[i])
    {
        write(1, &s[i], 1);
        i++;
    }
}

void alpha_mirror(char *s)
{
    int i = 0;
    int mirror;
    while (s[i])
    {
        mirror = 0;
        if(s[i]>= 'A' && s[i]<='Z')
        {
            mirror = s[i]-'A';
            s[i] = 'Z'-mirror;
        }
        else if(s[i]>= 'a' && s[i]<='z')
        {
            mirror = s[i]-'a';
            s[i] = 'z'-mirror;
        }
        write(1, &s[i], 1);
        i++;
    }
}


int main (int c, char** a)
{
    if(c !=2)
    {
        write(1, "\n", 1);
        return (0);
    }
    char *msg = a[1];
    alpha_mirror(msg);
    write(1, "\n", 1);
    return (0);
}
