/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 18:15:27 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/02 18:24:55 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
/*
char    *ft_strrchr(const char *str, int c)
{
	int	count;
       
	count = ft_strlen(str);
	str = str + count;
	while (*str != c && count != 0)
	{
		str--;
		count--;
	}
	return ((void*)str);
}
*/

char *ft_strrchr(const char *s, int c) {
    const char *last = NULL;
    while (*s != '\0') {
        if (*s == (char)c)
            last = s;
        s++;
    }
    if ((char)c == '\0')
        return (char *)s;
    return (char *)last;
}
