/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/03 19:35:26 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/21 21:57:29 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_atoi(const char *str)
{
	size_t	ind;
	int		neg;
	int		res;

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
	while (ind < (ft_strlen(str)) && ft_isdigit(str[ind]))
	{
		res = res * 10 + str[ind] - '0';
		ind++;
	}
	if (neg % 2)
		res = -res;
	return (res);
}
