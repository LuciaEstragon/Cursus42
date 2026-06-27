//empiezo a las 12:55 -> 2 prueba --> ERROR No leer %  -> 13:40 (NOTA: funciones permitidas atoi y printf, hubiera tardado menos)

#include<unistd.h>

void putstr(char *a)
{
    int i=0;
    while(a[i])
    {
        write(1, &a[i], 1);
        i++;
    }
}
void putnumb(int n)
{
    if(n<0)
    {
        n=-n;
        write(1, "-", 1);
    }
    if(n>=10)
        putnumb(n/10);
    char c= n%10 + '0';
    write(1, &c, 1);
}
int ft_atoi(char *str)
{
    int numb=0;
    int i=0;
    int neg=1;
    if(str[i]=='-')
    {
        numb = -1*numb;
        neg=-1;
        i++;
    }
    while(str[i]>='0' && str[i]<='9')
    {
        numb=numb*10+str[i]-'0';
        i++;
    }
    return(numb*neg);
}
int ft_strlen(char*str)
{
    int len=0;
    while(str[len])
        len++;
    return len;
}


int opera(int numa, char c, int numb)
{
    int res;
    if(c=='+')
    {
        res=numa+numb;
        putnumb(res);
    }
        if(c=='-')
    {
        res=numa-numb;
        putnumb(res);
    }
        if(c=='/')
    {
        if(numb==0) res=0;
        else res=numa/numb;
        putnumb(res);
    }
        if(c=='*')
    {
        res=numa*numb;
        putnumb(res);
    }
            if(c=='%')
    {
        if(numb==0) res=0;
        else res=numa%numb;
        putnumb(res);
    }
    write(1, "\n", 1);
    return 0;

}
int main(int argc, char** argv)
{
    if(argc != 4)
    {
        write(1, "\n", 1);
        return 0;
    }
    int numa = ft_atoi(argv[1]);
    if(ft_strlen(argv[2])!=1)
    {
        write(1, "\n", 1);
        return 0;
    }   
    char c = *argv[2];
    int numb = ft_atoi(argv[3]);
    opera(numa, c, numb);
    return 0;
}