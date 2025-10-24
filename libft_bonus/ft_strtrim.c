/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/06/24 09:02:26 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/22 17:47:56 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	ft_check_init(char *s1, char *set);
static size_t	ft_check_end(char *s1, char *set);

char	*ft_strtrim(char const *s1, char const *set)
{
	char	*result;
	size_t	start;
	size_t	end;
	size_t	len;

	if (!s1 || !set)
		return (NULL);
	start = ft_check_init((char *)s1, (char *)set);
	if (start >= ft_strlen((char *)s1))
		return (ft_strdup(""));
	end = ft_check_end((char *)s1, (char *)set);
	len = end - start + 1;
	result = ft_substr((char *)s1, start, len);
	if (!result)
		return (NULL);
	return (result);
}

static size_t	ft_check_init(char *s1, char *set)
{
	size_t	len;
	size_t	ind;
	size_t	flag;
	size_t	j;

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

static size_t	ft_check_end(char *s1, char *set)
{
	size_t	len;
	size_t	ind;
	size_t	flag;
	size_t	j;

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
