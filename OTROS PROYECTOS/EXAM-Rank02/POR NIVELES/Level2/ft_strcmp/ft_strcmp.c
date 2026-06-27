int    ft_strcmp(char *s1, char *s2)
{
    int i = 0;
    if(!s1 || !s2)
        return(0);
    while (s1[i] == s2[i])
    {
        i++;
        if(s1[i] == '\0' && s2[i] == '\0')
            return (0);
        if(s1[i] == '\0')
            return (-1);
        if(s2[i] == '\0')
            return (1);
    }
    if(s1[i] > s2[i])
        return (s1[i] - s2[i]);
    else if(s1[i] < s2[i])
        return (s1[i] - s2[i]);
    else 
    return (0);
}
/*
#include <stdio.h>
int main()
{
    char *a="aaA", *b="aaa";
    printf("%d", ft_strcmp(a, b));
    return 0;
}*/