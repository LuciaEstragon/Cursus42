#include<unistd.h>

void str_cap(char *s)
{
    int i=0;
    if(s[i] >= 'a' && s[i] <= 'z')
    {
        s[i]-=32;
        write(1, &s[i], 1);
        i++;
    }
    else
    {
        write(1, &s[i], 1);
        i++;
    }
    while (s[i])
    {
        if((s[i] >= 'A' && s[i] <= 'Z'))
        {
            s[i]+=32;
        }
        else if((s[i-1]!=' ')&& (s[i] >= 'a' && s[i] <= 'z'))
        {
            s[i]= s[i]-32;
        }

        write(1, &s[i], 1);
        i++;
    }
}

#include <unistd.h>

void str_cap2(char *s)
{
    int i = 0;

    while (s[i])
    {
        // CASO 1: Es la primera letra de la cadena O sigue a un espacio
        if (i == 0 || s[i - 1] == ' ')
        {
            // Si es minúscula, la pasamos a MAYÚSCULA
            if (s[i] >= 'a' && s[i] <= 'z')
                s[i] -= 32;
        }
        // CASO 2: No sigue a un espacio (está en medio de una palabra)
        else
        {
            // Si es mayúscula, la pasamos a minúscula para limpiar la palabra
            if (s[i] >= 'A' && s[i] <= 'Z')
                s[i] += 32;
        }

        // Escribimos el carácter ya procesado
        write(1, &s[i], 1);
        i++;
    }
}




int main(int argc, char** argv)
{
    if(argc<2)
    {
        write(1,"\n",1);
        return 0; 
    }
    int i = 1;
    while(argv[i])
    {
        str_cap2(argv[i]);
        i++;
        write(1,"\n",1);
    }
    return 0;
}