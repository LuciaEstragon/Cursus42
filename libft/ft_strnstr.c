/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/06/25 15:06:26 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/15 17:45:44 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	ind;
	size_t	ind_check;
	size_t	sub_ind;
	char	*big_ptr;

	big_ptr = (char*)big;
	ind = 0;
	while (little[ind] == '\0')
	{
		return (big_ptr);
	}
	while (big_ptr[ind] != '\0' && ind < len)
	{
		ind_check = ind;
		sub_ind = 0;
		while (big_ptr[ind_check] == little[sub_ind])
		{
			sub_ind++;
			ind_check++;
			if (little[sub_ind] == '\0')
				return (&big_ptr[ind]);
		}
		ind++;
	}
	return (NULL);
}
