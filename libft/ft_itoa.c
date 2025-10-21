/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 07:56:07 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/20 20:31:36 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int		digit_count(int nb);

char	*ft_itoa(int n)
{
	char	*str;
	int		len_nmb;
	long	nb;

	nb = n;
	len_nmb = digit_count(nb);
	str = (char *)ft_calloc(sizeof(char), (len_nmb + 1));
	if (!str)
		return (NULL);
	if (nb < 0)
	{
		str[0] = '-';
		nb = -nb;
	}
	else if (nb == 0)
		str[0] = '0';
	while (nb != 0)
	{
		len_nmb--;
		str[len_nmb] = (nb % 10) + '0';
		nb = nb / 10;
	}
	return (str);
}

int	digit_count(int nb)
{
	int		count;

	count = 0;
	if (nb <= 0)
		count = 1;
	while (nb != 0)
	{
		count++;
		nb = nb / 10;
	}
	return (count);
}
