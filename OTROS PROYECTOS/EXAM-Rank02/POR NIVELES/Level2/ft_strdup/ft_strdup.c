#include <stdlib.h>

char    *ft_strdup(char *src)
{
    char *ptr;
    int i = 0;

    while (src[i] != '\0')
        i++;
    ptr = (char*)malloc(sizeof(int) * i);
    if (ptr == NULL)
        return(NULL);
    i=0;
    while (src[i])
    {
        ptr[i] = src[i];
        i++;
    }
    ptr[i] = '\0';
    return (ptr);
}

/*
#include <stdio.h>
int main()
{
    char *msg = "HOla que tal !";
    char *cp_dup;

    cp_dup = ft_strdup(msg);
    printf("%s", cp_dup);
    free(cp_dup);
    return 0;
}
    */
