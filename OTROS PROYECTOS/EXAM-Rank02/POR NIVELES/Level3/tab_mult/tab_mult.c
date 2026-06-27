#include <unistd.h>

int ft_atoi(char *msg)
{
    int n = 0;
    int i=0;
    while (msg[i])
    {
        n = n*10 + msg[i] - '0';
        i++;
    }
    return n;
}
void putnmb(int numb)
{  
    if(numb>=10)
        putnmb(numb/10);
    char c = numb%10 + '0';
    write(1, &c, 1);
}

void tab_mult(int numb)
{
    int res = 0;
    int i = 1;
    while(i<=9)
    {
        putnmb(i);
        write(1, " x ", 3);
        putnmb(numb);
        write(1, " = ", 3);
        res = numb*i;
        putnmb(res);
        write(1, "\n", 1);
        i++;
    }
}

int main(int argc, char** argv)
{
    if(argc !=2)
    {
        write(1, "\n", 1);
        return 0;
    }
    char *msg=argv[1];
    int numb = ft_atoi(msg);
    //putnmb(numb);
    tab_mult(numb);
    //write(1, "\n", 1); //! importante!
    return 0;
}
