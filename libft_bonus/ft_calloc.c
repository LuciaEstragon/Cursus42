/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/06/24 09:02:26 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/24 19:02:50 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	char	*str;
	size_t	len;

	len = nmemb * size;
	if (len / nmemb != size)
		return (NULL);
	str = (char *)malloc(len);
	if (!str)
		return (NULL);
	ft_bzero(str, len);
	return ((void *)str);
}

/*
man calloc sais that calloc have to return = 0 when size or nmemb will be 0.
	if (nmemb == 0 || size == 0)
		return (NULL);
 -- paco has an error with that.
I passed moulinette without this code and without this other:
	if (len / nmemb != size)
		return (NULL);
*/