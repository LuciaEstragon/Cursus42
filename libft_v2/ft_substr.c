
#include "libft.h"


char *ft_substr(char const *s, unsigned int start, size_t len)
{
    char *sub;
    size_t i;
    size_t s_len;

    if (!s)
        return (NULL);
    
    s_len = ft_strlen(s);
    
    // Si start está más allá del string, devolver string vacío
    if (start >= s_len)
        return (NULL);//return (strdup(""));
    
    // Ajustar len si es demasiado grande
    if (len > s_len - start)
        len = s_len - start;
    
    sub = malloc(sizeof(char) * (len + 1));
    if (!sub)
        return (NULL);
    
    i = 0;
    while (i < len && s[start + i])
    {
        sub[i] = s[start + i];
        i++;
    }
    sub[i] = '\0';
    
    return (sub);
}

/*
char *ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*ptr;
	size_t	ind;

	ptr = (char*)malloc(len);
	if(!ptr || !s)//(ptr == NULL)
		return(NULL);

	ind = 0;
	while (s[start + ind] != '\0' && ind < len)
	{
		ptr[ind] = s[start + ind];
		ind++;
	}
	while (ind < len)
	{
		ptr[ind] = '\0';
		ind++;
	}
	return(ptr);
}*/
/*
int	main(void)
{
	char* msg;
	msg = "hola, que tal?";
	char* ptr;

	printf("%s", msg);
	ptr = ft_substr(msg, 3, 15);
	printf("%s",ptr);

	return (0);
}
*/
