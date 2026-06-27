/*
Escribe una función que tome una cadena, la divida en palabras y las devuelva como
un array de cadenas terminado en NULL.

Una "palabra" se define como una parte de una cadena delimitada por espacios/tabulaciones/nuevas
líneas, o por el inicio/fin de la cadena.


ejemplo: 
*str = "Hola que tal estas"
cadena = [hola][que][tal][estas]
*/


// TIEMPO : 1 hora
#include <stdlib.h>
#include <stdio.h>

char    **ft_split(char *str)
{
    int i=0;
    int j=0;
    int w=0;
    int num_palabras=0;
    int num_letras=0;

    while(str[i]!='\0')
    {
        while(str[i]!=' ' && str[i]!='\t' && str[i]!='\n' && str[i]!='\0')
            i++;
        num_palabras++;
        if(str[i]!='\0')
            i++;
    }    


    char **cadena = (char**)malloc(sizeof(char**)*num_palabras);
    if (!cadena)
        return (NULL);
    i=0;
    printf("NumTOT= %d \n\n\n", num_palabras);
    while(j<num_palabras)
    {
        num_letras=0;
        while(str[i]!=' ' && str[i]!='\t' && str[i]!='\n' && str[i]!='\0')
        {
            num_letras++;
            i++;
        }
        printf("i=%d \n\n\n", i);
        printf("l=%d \n\n\n", num_letras);
        char *palabra = (char*)malloc(sizeof(char*)*num_letras);
        if (!palabra)
            return (NULL);
        w=i-num_letras;
        int k=0;
        while(k<num_letras)
        {
            palabra[k]=str[w];
            w++;
            k++;
        }
        printf("palabra=%s \n\n\n", palabra);
        i++;
        cadena[j]=palabra;
        j++;
    }
    printf("SALE\n\n\n");

    return(cadena);
}



int main(int argc, char **argv)
{
    if(argc<2)
        return (0);
    else
    {
        char *str = argv[1];
        printf("%s\n \n \n", str);
        printf("hola \n \n \n");
        char **cadena = ft_split(str);
        int i=0, j=0;
        while(i<3)
        {
            printf("%s", cadena[i]);
            i++;
        }
    }
    return (0);
}