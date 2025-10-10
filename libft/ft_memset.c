/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 07:56:07 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/06 08:02:39 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*
#include <stddef.h>

void	*ft_memset(char *src, int c, size_t n)
{
	size_t	i;

	i = 0;
	while (src[i] != '\0' && i <= n)
	{
		src[i] = c;
		i++;
	}
	return (src);
}
*/

#include <stddef.h>

void *ft_memset(void *s, int c, size_t n) 
{
    unsigned char *ptr = (unsigned char *)s;
    unsigned char value = (unsigned char)c;
    size_t i;
    
    i = 0;
    while ( i < n) 
    {
        ptr[i] = value;
        i++;
    }
    return (ptr);
}
