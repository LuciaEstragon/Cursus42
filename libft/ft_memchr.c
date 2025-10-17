/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 08:16:27 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/14 16:09:51 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

void *ft_memchr(const void *s, int c, size_t n)
{
    const unsigned char *str;
    unsigned char ch;
    size_t i;

    str = (const unsigned char *)s;
    ch = (unsigned char)c;
    i = 0;
    
    while (i < n)
    {
        if (str[i] == ch)
            return ((void *)(str + i));
        i++;
    }
    return (NULL);
}

/*
void	*ft_memchr(const void *scr, int c, size_t n)
{
	char	*ptr;
	size_t	i;

	ptr = (char *)scr;
	if (!c)
		return ((char *)ptr);
	i = 0;
	while (ptr[i] != '\0' && i < n)
	{
		if (ptr[i] == (char)c)
			return ((void *)ptr);
		i++;
	}
	//if ((char)c == '\0')
		//return ((char *)ptr);
	return ((void *)0);
}
*/
/*
char	*ft_strchr(const char *s, int c)
{
	while (*s != '\0')
	{
		if (*s == (char)c)
			return ((char *)s);
		s++;
	}
	if ((char)c == '\0')
		return ((char *)s);
	return (0);
}*/
