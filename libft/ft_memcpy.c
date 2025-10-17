/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 08:03:10 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/14 16:35:28 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	size_t	i;
	char	*ptr_src;
	char	*ptr_dest;

	if(!dest && !src)
		return (NULL);
	ptr_dest = (char *)dest;
	ptr_src = (char *)src;
	i = 0;
	/*if(n == 0)
		return ((void *)0);*/
	while (i < n)
	{
		ptr_dest[i] = ptr_src[i];
		i++;
	}
	/*while (!ptr_src)
		ptr_dest[i] = '\0';*/
	return (ptr_dest);
}
