/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/06/24 09:02:26 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/16 19:03:50 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	char	*str;
	size_t len;

	len = ft_strlen(s);
	str = (char *)malloc(len + 1);
	if (!str)
		return (NULL);
	ft_strlcpy(str, s, len + 1);
	return (str);
}
/*
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    const char *cadena_original = "Hola Mundo";
    char *cadena_copiada;

    // Duplicar la cadena
    cadena_copiada = strdup(cadena_original);

    if (cadena_copiada == NULL) {
        fprintf(stderr, "Error al duplicar la cadena\n");
        return 1;
    }

    printf("Cadena original: %s\n", cadena_original);
    printf("Cadena copiada: %s\n", cadena_copiada);

    // Liberar la memoria asignada por strdup
    free(cadena_copiada);

    return 0;
}
*/
