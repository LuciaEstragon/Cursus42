#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int    ft_putnbr_count(int nb, int count);
char    *ft_putnbr_string(int nb, char *str, int len);
void especial_strlcat(char *dest, size_t dest_size, char c);

char *ft_itoa(int n)
{
	if(!n)
		return (NULL);
	char	*str;
	int	size;

	size = 0;
	size = ft_putnbr_count(n, size);
	str = (char *)malloc(size * sizeof(char*));
	if(!str)
		return (NULL);
	printf("count: %d \n",size);
	str = ft_putnbr_string(n, str, size);
	return (str);
}

int    ft_putnbr_count(int nb, int count)
{
        count++;
        if (nb == -2147483648)
		nb = -2147483647;
        if (nb < 0)
        {
                count ++;
                nb = nb * (-1);
        }
        while (nb >= 10)
        {
		nb = nb / 10;
		count++;
	}
	return (count);
}

char    *ft_putnbr_string(int nb, char *str, int len)
{
	char	c;
	//char	*s;

        if (nb == -2147483648)
	{
		str = "-2147483648";
		return (str);
	}
	if (nb < 0)
        {
                //str = "-";
                especial_strlcat(str, len+1, '-');
		nb = nb * (-1);
        }
        if (nb >= 10)
                ft_putnbr_string(nb / 10, str, len);
        c = (nb % 10) + '0';
        //s = (char *)c;
	//printf("%c", c);
	especial_strlcat(str, len+1, c);
	//printf("%s", str);
        return (str);
}

void especial_strlcat(char *dest, size_t dest_size, char c)
{
    if (strlen(dest) < dest_size - 1) 
    {
        dest[strlen(dest)] = c;
        dest[strlen(dest) + 1] = '\0';
    }
}



int	main(void)
{
	char	*s;

	s = ft_itoa('\0');
	printf("%s", s);
	free(s);
	return(0);
}
