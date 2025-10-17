/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/06/24 09:02:26 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/16 20:12:23 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_comprueba_inicio(char *s1, char *set);
int	ft_comprueba_fin(char *s1, char *set);

char	*ft_strtrim(char const *s1, char const *set)
{
	char	*result;
	unsigned int start;
	unsigned int end;
	int len;

	if (!s1 || !set)
        	return (NULL);
	start = ft_comprueba_inicio((char *)s1, (char *)set);
	if(start >= ft_strlen((char *)s1))
		return (NULL);
	end = ft_comprueba_fin((char *)s1, (char *)set);
	len = end - start + 1;
	result = (char *)malloc(len);
	result = ft_substr((char *)s1, start, len);
	return(result);
}

int	ft_comprueba_inicio(char *s1, char *set)
{
	int	len;
	int	ind;
	int	flag;
	int	j;

	len = ft_strlen((char *)set);
	flag = 1;
	j = 0;
	while(flag)
	{
	ind = 0;
	flag = 0;
	while (ind < len)
	{
		if(s1[j] == set[ind]) //si encuentra coincidencia
		{
			flag = 1; // encontrado
			j++;
		}
		//si no existe respuesta paso al siguiente
		ind++;
	}
	}
	return(j);
}

int	ft_comprueba_fin(char *s1, char *set)
{
	int	len;
	int	ind;
	int	flag;
	int	j;

	len = ft_strlen((char *)set);
	flag = 1;
	j = ft_strlen((char *)s1) - 1;
	while(flag)
	{
	ind = 0;
	flag = 0;
	while (ind < len)
	{
		if(s1[j] == set[ind]) //si encuentra coincidencia
		{
			flag = 1; // encontrado
			j--;
		}
		//si no existe respuesta paso al siguiente
		ind++;
	}
	}
	return(j);
}
/*
#include <stdio.h>

// Aquí iría tu función ft_strtrim corregida

int main(void)
{
    char *result;
    
    printf("=== PRUEBAS ft_strtrim ===\n\n");
    
    // Prueba 1: Caso normal
    printf("1. Caso normal:\n");
    result = ft_strtrim("  hello world  ", " ");
    printf("'  hello world  ' -> '%s'\n\n", result);
    free(result);
    
    // Prueba 2: Múltiples caracteres en set
    printf("2. Múltiples caracteres en set:\n");
    result = ft_strtrim("abcHOLAabc", "abc");
    printf("'abcHOLAabc' -> '%s'\n\n", result);
    free(result);
    
    // Prueba 1: Caso Ultra
    printf("1. Caso ultra - se contiene a si mismo:\n");
    result = ft_strtrim("accbabbaccaabc", "abc");
    printf("'  accbabbaccaabc  ' -> '%s'\n\n", result);
    free(result);
    
    // Prueba 3: String vacío después del trim
    printf("3. String vacío después del trim:\n");
    result = ft_strtrim("aaa", "a");
    printf("'aaa' -> '%s'\n\n", result);
    free(result);
    
    // Prueba 4: String original vacío
    printf("4. String original vacío:\n");
    result = ft_strtrim("", "abc");
    printf("'' -> '%s'\n\n", result);
    free(result);
    
    // Prueba 5: Set vacío
    printf("5. Set vacío:\n");
    result = ft_strtrim("hello world", "");
    printf("'hello world' -> '%s'\n\n", result);
    free(result);
    
    // Prueba 6: Sin caracteres para recortar
    printf("6. Sin caracteres para recortar:\n");
    result = ft_strtrim("hello", "xyz");
    printf("'hello' -> '%s'\n\n", result);
    free(result);
    
    // Prueba 7: Solo recorte al inicio
    printf("7. Solo recorte al inicio:\n");
    result = ft_strtrim("xxxhello", "x");
    printf("'xxxhello' -> '%s'\n\n", result);
    free(result);
    
    // Prueba 8: Solo recorte al final
    printf("8. Solo recorte al final:\n");
    result = ft_strtrim("helloyyy", "y");
    printf("'helloyyy' -> '%s'\n\n", result);
    free(result);
    
    // Prueba 9: Caracteres especiales
    printf("9. Caracteres especiales:\n");
    result = ft_strtrim("\t\nhello\t\n", "\t\n");
    printf("'\\t\\nhello\\t\\n' -> '%s'\n\n", result);
    free(result);
    
    // Prueba 10: NULL parameters
    printf("10. NULL parameters:\n");
    result = ft_strtrim(NULL, "abc");
    printf("NULL -> %s\n", result);
    result = ft_strtrim("hello", NULL);
    printf("'hello', NULL -> %s\n\n", result);
    
    // Prueba 11: String de un solo carácter
    printf("11. String de un solo carácter:\n");
    result = ft_strtrim("a", "a");
    printf("'a' -> '%s'\n\n", result);
    free(result);
    
    // Prueba 12: Caracteres mezclados
    printf("12. Caracteres mezclados:\n");
    result = ft_strtrim("xyhelloxy", "xyz");
    printf("'xyhelloxy' -> '%s'\n\n", result);
    free(result);

    return 0;
}*/

/*evalua todo el *set pasando por cada i, y evaluandolo sobre cada j de la palabra*/
