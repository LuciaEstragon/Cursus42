/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/03 19:35:26 by lestrada          #+#    #+#             */
/*   Updated: 2025/07/03 21:36:54 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isdigit(int c)
{
	if (c >= 48 && c <= 57)
		return (1);
	return (0);
}

int	ft_atoi(char *str)
{
	size_t	ind;
	int	neg;
	int	res;
size_t len = 0;
len = ft_strlen(str);

	ind = 0;
	while (str[ind] != '\0'
		&& ((str[ind] == ' ') || (str[ind] == '\f') || (str[ind] == '\n')
			|| (str[ind] == '\r') || (str[ind] == '\t') || (str[ind] == '\v')))
		ind++;
		
    neg = 0;
	if (str[ind] != '\0' && ((str[ind] == '+') || (str[ind] == '-')))
	{
		if (str[ind] == '-')
			neg++;
		ind++;
	}

	res = 0;
	while (ind<(len) && ft_isdigit(str[ind]))
	{
		res = res * 10 + str[ind] - '0';
		ind++;
	}
	if (neg % 2)
		res = -res;
	return (res);
}

