/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 17:18:25 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/15 17:33:06 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

/*void	*ft_memmove(void *dest, const void *src, size_t n)
{
	size_t	i;
	char	*ptr_dest;
	char	*ptr_src;
	char	*ptr_aux;

	if(!dest && !src)
		return (NULL);
		
	ptr_dest = (char*)dest;
	ptr_src = (char*)src;
	ptr_aux = NULL;
	i = 0;
	while (i < n)
	{
		ptr_aux[i] = ptr_src[i];
		i++;
	}
	while (i < n)
	{
				ptr_dest[i] = ptr_aux[i];
		i++;
	}
	//ptr_dest[i] = '\0';
	return (ptr_dest);
}*/
/*
void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char	*ptr_dest;
	unsigned char	*ptr_src;

	ptr_dest = (unsigned char *)dest;
	ptr_src = (unsigned char*)src;
	if (ptr_dest == ptr_src || n == 0)
		return (dest);
	if (!ptr_dest && !ptr_src)
		return (NULL);
	if (ptr_dest < ptr_src)
	{
		while (n--)
		{
			*ptr_dest++ = *ptr_src++;
		}
	}
	else
	{
		ptr_dest += n;
		ptr_src += n;
		while (n--)
		{
			*ptr_dest-- = *ptr_src--;
		}
	}
	return (dest);
}*/

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
Las condiciones que no te miran los else if seria:
	if (ptr_dest == ptr_src || n == 0)
		return (dest);

*/

