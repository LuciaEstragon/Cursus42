#include <unistd.h>

void putnmb(int numb)
{
    if(numb>=10)
        putnmb(numb/10);
    char c = numb%10 + '0';
    write(1, &c, 1);
}

int ft_atoi(char *str)
{
    int i=0;
    int numb=0;
    while(str[i]>='0' && str[i]<='9')
    {
        numb = numb*10 + str[i]-'0';
        i++;
    }
    return(numb);
}

int prim(int num)
{
    int result=0;
    int i=2;
    int no_primo = 0;
    while(num>0)
    {
        //es primo??
        no_primo=0;
        i=2;
        while(num>i)
        {
            if(num%i == 0)
                no_primo=1;
            i++;
        }
        if(no_primo == 0)
            result = result + num;
        num--;
    }
    return (result-1);
}

int main(int argc, char** argv)
{
    if(argc<2)
    {
        //write(1, "0", 1);
        putnmb(0);
        write(1, "\n", 1);
        return(0);
    }
    int numb = ft_atoi(argv[1]);
    if(numb<=0)
    {
        //write(1, "0", 1);
        putnmb(0);
        write(1, "\n", 1);
        return(0);
    }
    putnmb(prim(numb));
    write(1, "\n", 1);
    return(0);
}