/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/06/25 15:06:26 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/21 21:19:47 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
* It works almost exactly like strstr: find a string inside str
*
* The difference is that I only compare the first len ​​values.
* Caution! In this case: f(xxAAAAA, AAAAA, 5); returns false.
*/

#include <string.h>
#include <stdio.h>

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	i;
	size_t	j;

	if (*little == '\0')
		return ((char *)big);
	i = 0;
	while (big[i] && i < len)
	{
		j = 0;
		while (big[i + j] == little[j] && (i + j) < len)
		{
			if (little[j + 1] == '\0')
				return ((char *)(big + i));
			j++;
		}
		i++;
	}
	return (NULL);
}

/*
MIA

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
	if ((ft_strlen(little) > len) || len == 0)
		return (NULL);
	while (ind < len - ft_strlen(little) && big_ptr[ind] != '\0')
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
*/
/*

#include <string.h>
#include <stdio.h>

int main()
{
	const char *str = "Hello worworld happy Lu";
	const char *str2 = "world";

	//char *result1 = strchr(str, '\0');  // 'e' se promueve a int
	//char *result2 = strrchr(str, '\0');  // 'e' se promueve a int
	char *result2 = ft_strnstr(str, str2, 0);  // 'e' se promueve a int
	char *result3 = ft_strnstr(str, str2, 11);  // 'e' se promueve a int
	char *result4 = ft_strnstr(str, str2, 15);  // 'e' se promueve a int
	
	//printf("result %s \n", result1);
	printf("result %s \n", result2);
	printf("result %s \n", result3);
	printf("result %s \n", result4);
	return(0);
}
*/