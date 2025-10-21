/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/06/25 15:06:26 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/21 10:57:37 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
* Es casi el mismo funcionamiento de strstr: encontrar un string dentro de str
*
* En lo que se diferencian es que yo ahora solo comparo los primeros len.
* Cuidado! En este caso: f(xxAAAAA, AAAAA, 5); da falso.
*/

	//asi solo falla la prueba 10
char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	ind;
	size_t	ind_check;
	size_t	sub_ind;
	char	*big_ptr;

	big_ptr = (char *)big;
	ind = 0;
	if (little[ind] == '\0')
		return (big_ptr);
	if ((ft_strlen(little) > len))
		return (NULL);
	while (ind <= len - ft_strlen(little) && big_ptr[ind] != '\0')
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
