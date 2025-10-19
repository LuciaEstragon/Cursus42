/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 10:31:57 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/02 10:34:20 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
 /*
 * Ejemplo de uso: s-".Hola....q.ue t...al"
 * ft_split va a crear un string **result=[Hola][q][ue t][al]
 *
 * 1º Cuentas el numero de palabras count_words(), metodo que encuentra flancos.
 * 2º Bucle para rellenar cada palabra con sus letras.
 *
 * Como es un doble puntero necesitas dos mallocs
 * 
*/
int	count_words(char const *s, char c);
int	len_words(char const *s, char c);
char	fill_words(char const *s, char c);

char	**ft_split(char const *s, char c)
{
	char	**result;
	int		total_word;
	int		ind_words;
	int		ind;

	total_word = count_words(s, c);
	result = (char **)calloc(total_word + 1, sizeof(char *));
	if (!result)
		return (0);
	ind_words = 0;
	while (ind_words < total_word)
	{
		fill_words(s, c);
		ft_memcpy(*result[ind_words], fill_words(s, c)); 
		ind_words++;
	}
	result[ind_words] = '\0';
	return(*result);
}    

int	count_words(char const *s, char c)
{
	int	ind;
	int	count;
	int	flag;

	ind = 0;
	count = 0;
	flag = 0;
	while (s[ind] != '\0')
	{
		if (s[ind] != c && flag==0)
		{
			flag = 1;
			count ++;
		}
		if (s[ind] == c && flag==1)
			flag = 0;
		ind++;
	}
	return (count);
}

int	len_words(char const *s, char c)
{
	int	ind;
	int	count;

	ind = 0;
	count = 0;
	while (s[ind] != c)
		count ++;
	return (count);
}

char	fill_words(char const *s, char c)
{
	char *dest;
	int ind;
	int		len_word;

	ind = 0;
	if (s[ind] != c)
	{
		len_word = len_words(s, c);
		dest = (char *)malloc(len_word + 1);
		if (!result)
			return (0);
		while (s[ind] != c)
		{
			dest[ind] = s[ind];
			ind++;
		} 
		dest[ind] = '\0';
	}
	else
		ind++;
	return (dest);
}


#include <stdio.h>
#include <stdlib.h>

void imprimir_matriz_char(char **matriz, int filas) {
    for (int i = 0; i < filas; i++) {
        // Usa %s para imprimir la cadena completa a la que apunta matriz[i]
        printf("%s\n", matriz[i]);
    }
}

int main() {
    // Definición de una matriz de punteros a char
    char *s = "hola..que..tal.";
    char c = '.';
	char **mi_matriz;

	mi_matriz = ft_split(s, c);
	
    // Asignación de cadenas a cada puntero
    printf("Imprimiendo la matriz de cadenas:\n");
    imprimir_matriz_char(mi_matriz, filas);

    // Liberar la memoria asignada
    free(mi_matriz);

    return 0;
}