/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/06/25 15:06:26 by lestrada          #+#    #+#             */
/*   Updated: 2025/07/01 13:48:13 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	str_len(char *src);

char	*ft_strstr(char *str, char *to_find)
{
	int	ind;
	int	ind_check;
	int	sub_ind;

	ind = 0;
	while (to_find[ind] == '\0')
	{
		return (str);
	}
	while (str[ind] != '\0')
	{
		ind_check = ind;
		sub_ind = 0;
		while (str[ind_check] == to_find[sub_ind])
		{
			sub_ind++;
			ind_check++;
			if (to_find[sub_ind] == '\0')
				return (&str[ind]);
		}
		ind++;
	}
	return (NULL);
}

int	str_len(char *src)
{
	int	len;

	len = 0;
	while (src[len] != '\0')
		len++;
	return (len);
}
