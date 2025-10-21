/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 08:16:27 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/14 16:09:51 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	unsigned int	i;
	char			*str;
	char			c;

	str = (char *)malloc(ft_strlen(s)+1);
	if (!s || !f || !str)
		return (NULL);
	i = 0;
	while (s[i])
	{
		c = s[i];
		str[i] = (*f)(i, c);
		i++;
	}
	str[i++] = '\0';
	return (str);
}
