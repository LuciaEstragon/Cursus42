#include <stdlib.h>
#include <stdio.h>

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
}

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
