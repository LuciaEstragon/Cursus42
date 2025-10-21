/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 17:18:25 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/21 11:26:28 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char	*ptr_dest;
	unsigned char	*ptr_src;

	ptr_dest = (unsigned char *)dest;
	ptr_src = (unsigned char *)src;
	if (!ptr_dest && !ptr_src)
		return (NULL);
	if (ptr_dest > ptr_src)
	{
		while (n > 0)
		{
			n--;
			ptr_dest[n] = ptr_src[n];
		}
	}
	else if (ptr_dest < ptr_src)
	{
		while (n--)
		{
			*ptr_dest++ = *ptr_src++;
		}
	}
	return (dest);
}

/*
* The conditions that do not look at the else if would be:
* 	if (ptr_dest == ptr_src || n == 0)
* 		return (dest);
*/