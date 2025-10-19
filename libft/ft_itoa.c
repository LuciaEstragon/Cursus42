/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 07:56:07 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/10 15:27:06 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int		ft_putnbr_count(int nb, int count);
char	*ft_putnbr_string(int nb, char *str, int len);
void	especial_strlcat(char *dest, size_t dest_size, char c);

char	*ft_itoa(int n)
{
	if(!n)
		return (NULL);
	char	*str;
	int		size;

	size = 0;
	size = ft_putnbr_count(n, size);
	str = (char *)malloc(size * sizeof(char*));
	if(!str)
		return (NULL);
	str = ft_putnbr_string(n, str, size);
	return (str);
}

int	ft_putnbr_count(int nb, int count)
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

char	*ft_putnbr_string(int nb, char *str, int len)
{
	char	c;

	if (nb == -2147483648)
	{
		str = "-2147483648";
		return (str);
	}
	if (nb < 0)
	{
		especial_strlcat(str, len+1, '-');
		nb = nb * (-1);
	}
	if (nb >= 10)
		ft_putnbr_string(nb / 10, str, len);
	c = (nb % 10) + '0';
	especial_strlcat(str, len+1, c);
	return (str);
}

void	especial_strlcat(char *dest, size_t dest_size, char c)
{
	if (ft_strlen(dest) < dest_size - 1) 
	{
		dest[ft_strlen(dest)] = c;
		dest[ft_strlen(dest) + 1] = '\0';
	}
}
