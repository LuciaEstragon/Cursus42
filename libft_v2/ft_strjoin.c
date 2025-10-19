#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char *ft_strjoin(char const *s1, char const *s2)
{
    char *result;
    int i;
    int j;
    
    if (!s1 || !s2)
        return (NULL);
    
    // Calcular longitud total
    i = 0;
    while (s1[i]) i++;
    j = 0;
    while (s2[j]) j++;
    
    // Reservar memoria
    result = malloc(sizeof(char) * (i + j + 1));
    if (!result)
        return (NULL);
    
    // Copiar s1
    i = 0;
    while (s1[i])
    {
        result[i] = s1[i];
        i++;
    }
    
    // Copiar s2
    j = 0;
    while (s2[j])
    {
        result[i + j] = s2[j];
        j++;
    }
    
    result[i + j] = '\0';
    return (result);
}

/*
char *ft_strjoin(char const *s1, char const *s2)
{
	char	*ptr;
	size_t	ind;

	if(!s1 && !s2)
		return (NULL);
	ptr = (char*)malloc(strlen(s1)+strlen(s2)+1);
	if (!ptr)
		return(NULL);

	ind = 0;
	while(*s1 != '\0')
	{
		ptr[ind] = s1[ind];
		ind++;
		s1++;
	}
	while(*s2 != '\0')
	{
		ptr[ind] = s2[ind];
		ind++;
		s2++;
	}
	ptr[ind] = '\0'; //añades +1 para este caracter
	return(ptr);
}*/
/*
int	main(void)
{
	char	*msg;
	char	*ans;
	char	*msg_comp;
	
	msg = "Hola, que tal? \n";
	ans = NULL;
	msg_comp = ft_strjoin(msg, ans);
	printf("%s", msg_comp);
	ans = "Bien, gracias";
        msg_comp = ft_strjoin(msg, ans);
        printf("%s", msg_comp);
	return(0);
}
*/
