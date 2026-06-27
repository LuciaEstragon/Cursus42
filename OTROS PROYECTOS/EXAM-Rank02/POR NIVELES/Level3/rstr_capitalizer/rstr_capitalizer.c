#include<unistd.h>

void putstr(char * s)
{
    int i = 0;

    while(s[i])
    {
        if(s[i]>='a' && s[i]<='z')
            s[i]-=32;
        else if (s[i]>='A' && s[i]<='Z')
            s[i]+=32;
        write(1, &s[i], 1);
        i++;
    }
}

void rstr_cap(char * s)
{
    int i = 0;
    while(s[i] != '\0')
    {
        if((s[i]>='A' && s[i]<='Z') && (s[i+1]!=' ' || s[i+1] == '\0'))
            s[i] += 32;
        if((s[i]>='a' && s[i]<='z') && (s[i+1]==' ' || s[i+1] == '\0'))
            s[i] -= 32;
        write(1, &s[i], 1);
        i++;
    }
}

int main(int argc, char** argv)
{
    if(argc<2)
    {
        write(1, "\n", 1);
        return(0);
    }
    int i = 1;
    while(argv[i])
    {
    char *str = argv[i];
    rstr_cap(str);
    write(1, "\n", 1);
    i++;
    }
    return(0);
}
/*
FAIL
Expected Output: "A firsT littlE tesT"
Your Output:     "A fIrsT lIttLe tesT"
==============================================
Please press enter to continue your practice.
*/