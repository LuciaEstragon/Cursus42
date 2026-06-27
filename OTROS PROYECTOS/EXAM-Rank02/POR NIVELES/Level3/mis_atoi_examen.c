// TIEMPO : 1 hora

int atoi_simple(char* str)
{
    int num = 0;
    int neg = 1;
    int i = 0;
    while(str[i]==' ')
        i++;
    if(str[i]=='+')
        i++;
    if(str[i]=='-')
    {
        neg = -1;
        i++;
    }

    while(str[i]>='0' && str[i]<='9')
    {
        num = num*10 + str[i]-'0';
        i++;
    }
 
    return (num*neg);
}

int atoi_medio(char* str)
{
    int num = 0;
    int neg = 1;
    int i = 0;
    while(str[i]==' ' || str[i]=='\t' || str[i]=='\r' || str[i]=='\v' || str[i]=='\n')
        i++;
    while(str[i]=='+' || str[i]=='-')
    {
        if(str[i]=='-')
            neg = neg*(-1);
        i++;
    }

    while(str[i]>='0' && str[i]<='9')
    {
        num = num*10 + str[i]-'0';
        i++;
    }
 
    return (num*neg);
}

int atoi_base(char* str, int base)
{
    int num = 0;
    int neg = 1;
    int i = 0;
    while(str[i]==' ' || str[i]=='\t' || str[i]=='\r' || str[i]=='\v' || str[i]=='\n')
        i++;
    while(str[i]=='+' || str[i]=='-')
    {
        if(str[i]=='-')
            neg = neg*(-1);
        i++;
    }

    while(str[i]!='\0')
    {
        if (str[i]>='0' && str[i]<='9')
            num = num * base + str[i] - '0';
        
        else if (str[i] >= 'A' && str[i] <= 'F')
			num = num * base + str[i] - '7';
		else if (str[i] >= 'a' && str[i] <= 'f')
			num = num * base + str[i] - 'W';
        i++;
    }
 
    return (num*neg);
}

////////////////////////////////////////////
////////////////////////////////////////////
#include <unistd.h>
void putnmb(int num)
{
    if(num<0)
    {
        write(1, "-", 1);
        num = -num;
    }
    if(num>=10)
        putnmb(num/10);
    char c;
    c = num % 10 + '0';
    write(1, &c, 1);
}

void printhex(int num)
{
    if(num<0)
    {
        write(1, "-", 1);
        num = -num;
    }
    if(num>=16)
        putnmb(num/16);

    char *hex_digits = "0123456789abcdef";
    char c;
    c = hex_digits[num % 16];
    write(1, &c, 1);
}

#include <stdio.h>
int main(int argc, char **argv)
{
    if(argc<2)
        return (0);
    else
    {
        char *str = argv[1];
        int num = atoi_base(argv[1], 10);
        //printf("%d", num);
        putnmb(num);
        printhex(num);
    }
    return (0);
}