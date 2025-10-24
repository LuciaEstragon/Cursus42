/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/06/24 09:02:26 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/20 20:50:25 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_comprueba_inicio(char *s1, char *set);
int	ft_comprueba_fin(char *s1, char *set);

char	*ft_strtrim(char const *s1, char const *set)
{
	char			*result;
	unsigned int	start;
	unsigned int	end;
	int				len;

	if (!s1 || !set)
		return (NULL);
	start = ft_comprueba_inicio((char *)s1, (char *)set);
	if (start >= ft_strlen((char *)s1))
		return (ft_strdup(""));
	end = ft_comprueba_fin((char *)s1, (char *)set);
	len = end - start + 1;
	result = (char *)malloc(len);
	result = ft_substr((char *)s1, start, len);
	return (result);
}

int	ft_comprueba_inicio(char *s1, char *set)
{
	int	len;
	int	ind;
	int	flag;
	int	j;

	len = ft_strlen((char *)set);
	flag = 1;
	j = 0;
	while (flag)
	{
		ind = 0;
		flag = 0;
		while (ind < len)
		{
			if (s1[j] == set[ind])
			{
				flag = 1;
				j++;
				break ;
			}
			ind++;
		}
	}
	return (j);
}

int	ft_comprueba_fin(char *s1, char *set)
{
	int	len;
	int	ind;
	int	flag;
	int	j;

	len = ft_strlen((char *)set);
	flag = 1;
	j = ft_strlen((char *)s1) - 1;
	while (flag)
	{
		ind = 0;
		flag = 0;
		while (ind < len)
		{
			if (s1[j] == set[ind])
			{
				flag = 1;
				j--;
				break ;
			}
			ind++;
		}
	}
	return (j);
}
