
#include <stdio.h>

// Función de ejemplo que convierte a mayúscula cada 2do carácter
void mayuscula_cada_dos(unsigned int i, char *c)
{
    if (i % 2 == 0) // Solo caracteres en posición par (0, 2, 4...)
    {
        if (*c >= 'a' && *c <= 'z')
            *c = *c - 32; // Convertir a mayúscula
    }
}

// Función que muestra índice + carácter
void mostrar_indice_char(unsigned int i, char *c)
{
    printf("Posición %d: '%c'\n", i, *c);
}

int main(void)
{
    char texto[] = "hola mundo";

    printf("Original: %s\n", texto);

    // Aplicar función que muestra índice y carácter
    ft_striteri(texto, mostrar_indice_char);

    // Aplicar función que convierte cada 2do carácter a mayúscula
    ft_striteri(texto, mayuscula_cada_dos);

    printf("Modificado: %s\n", texto);

    return 0;
}


/*

--ITOA--

int	main(void)
{
	char	*s;

	s = ft_itoa('\0');
	printf("%s", s);
	free(s);
	return(0);
}*/
