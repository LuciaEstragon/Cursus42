/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/06/24 19:38:27 by lestrada          #+#    #+#             */
/*   Updated: 2025/06/26 18:08:48 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*
 *len = strlcpy(dest, src, sizeof(dest));
 *Longitud de la cadena original size_scr = len
 *if (size_dest == len ) ==> la cadena se copio de forma exitosa
 *if (size_dest != len ) ==> la cadena fue truncada
*
*  NOTA: se copia el tamaño - el caracter nulo, es decir: 
*       dest[10] = src[9]+\0
 */

#include <stddef.h>

size_t	ft_strlcpy(char *dest, const char *src, size_t size)
{
	size_t	len;
	size_t	i;

	len = 0;
	while (src[len] != '\0')
		len++;
	i = 0;
	if (size > 0)
	{
		while (i < size - 1 && src[i] != '\0')
		{
			dest[i] = src[i];
			i++;
		}
		dest[i] = '\0';
	}
	return (len);
}
