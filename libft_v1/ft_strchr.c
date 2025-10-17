/* ************************************************************************** *//*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 15:25:51 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/02 16:14:25 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*
char    *ft_strchr(const char *str, int c)
{
	if (c == '\0')
		return ((void*)str);
	while (*str != c && *str != '\0')
		 str++;
	if(*str == '\0')
		return (0);
	return ((void*)str);
}
*/

char *ft_strchr(const char *s, int c) {
    while (*s != '\0') {
        if (*s == (char)c)
            return (char *)s;
        s++;
    }
    if ((char)c == '\0')
        return (char *)s;
    return (0);
}
