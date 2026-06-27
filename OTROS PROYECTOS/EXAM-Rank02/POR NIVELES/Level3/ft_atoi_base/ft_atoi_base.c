//Hora INICIO: 14:28
//Hora FIN: 15:00
// Intentos: 0
//ERRORES :  


int	ft_atoi(const char *str, int str_base)
{
    int neg=1;
    char *hex="0123456789abcdef";
    int i=0;
    int res=0;
    while(str[i]==' ')
        i++;
    if(str[i]=='-')
    {
        neg=1;
        i++;
    }
    while(str[i]!=0)
    {
        res= res*10 + str[i]-'0';
        i++;
    }
    return (res*neg);
}

int	ft_atoi_base(const char *str, int str_base)
{
    int neg=1;
    char *hex="0123456789abcdef";
    int i=0;
    int res=0;
    while(str[i]==' ')
        i++;
    if(str[i]=='-')
    {
        neg=1;
        i++;
    }
    while(str[i]!=0)
    {
        res= res*str_base + str[i]-'0';
        i++;
    }
    return (res*neg);
}

#include<stdio.h>
int main()
{
    char *str="a";
    //ascii to base
    int res = ft_atoi_base(str, 16);
    printf("%d", res);
    return 0;
}

