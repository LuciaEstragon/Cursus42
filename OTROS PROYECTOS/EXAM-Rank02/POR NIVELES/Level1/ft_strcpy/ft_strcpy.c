
char    *ft_strcpy(char *s1, char *s2)
{
    int i;
    i = 0;
    while(s2[i] != '\0')
    {
        s1[i] = s2[i];
        i++;
    }
    s1[i] = '\0';
    return (s1);
}
/*
#include<stdio.h>
int  main()
{
    char *msg = "Hola";
    char *cpy = "xxxxxxxxxxxxxx";

    char *res;
    res = ft_strcpy(cpy,msg);
    //printf("%s", res);
    //char *res2 = ft_strcpy(msg,cpy);
    printf("%s", msg);
    return 0;
}
*/