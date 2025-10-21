/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_striteri.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 10:31:57 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/02 10:34:20 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_striteri(char *s, void (*f)(unsigned int, char*))
{
	unsigned int	i;

	if (!s || !f)
		return ;
	i = 0;
	while (s[i])
	{
		(*f)(i, &s[i]);
		i++;
	}
}

/*
 * PUEDES PONERLO ASI, 
	while (s[i] != '\0')
	{
		f(i, &s[i]);
	//f(i, s); //pero no asi(no funciona) 
	//           asi &s o asi s[i] no compila
		i++;
	}
*/
