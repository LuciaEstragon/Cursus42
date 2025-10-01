/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 12:38:01 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/01 17:12:36 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
//#include <unistd.h>
//int ft_isdigit(int c);
//int ft_isalpha(int c);

int	main(void)
{
	char	letra = 'S';
	int	digit = 564;

	if (ft_isalpha(letra))
		write(1, "si", 2);
	else
		write(1, "no", 2);
	if (ft_isdigit(digit))
		write(1, "SI", 2);
	else
		write(1, "NO", 2);
	return (0);
}

