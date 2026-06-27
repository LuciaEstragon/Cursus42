/*unsigned char	swap_bits(unsigned char octet)
{
    //unsigned char a = octet>>4; // deplazas 4 hacia derecha 20 = 10100      -> 0001 0100 ->>4- 0000 0001
    //unsigned char b = octet<<4; // deplazas 4 hacia izquierda 20 = 10100    -> 0001 0100 -<<4- 0000 0100
    // concateno b y a.
    //unsigned char concat = a | b  
    // concat ->  es como decir: mi primer grupo (menos significativo) es a, y el segundo grupo (mas significativo) es b.
    //return(concat);  // a | b  -->  b(0100)a(0001) --> 0100 0001
    return((octet >> 4 | octet << 4));
}*/

/*
#include <stdio.h> 
int main()
{
    int a = 12;
    //a = 0000 1100
    printf("%b\n", a); 
    a=swap_bits(a);
    //a = 1100 0000
    printf("%b\n\n", a);
    a = 20;
    //a = 0001 0100
    printf("%b \n", a);
    a=swap_bits(a);
    //a = 0100 0001
    printf("%b \n\n", a);
    return 0;
}*/

/// NOTA!! Este metodo no es muy completo. Solo vale para numeros octales - con 8 bits. - SOLO
/// NOTA! Si tengo 16 bits me tendrian que preguntar que quiero rotar o como  => 1011 1101 1110 0011
#include<stdint.h>
uint16_t	swap_bits(uint16_t dieciseis)
{
    uint16_t a = dieciseis>>12; // deplazas 4 hacia derecha 750 = 0000 0010 1110 1110       -> 0000 0010 1110 1110 ->>12- 0000
    uint16_t b = dieciseis>>4; // deplazas 4 hacia izquierda 7500 = 0000 0010 1110 1110    -> 0000 0010 1110 1110 ->>4- 0000 0010 1110
    b = b<<4;                   // deplazas 4 hacia izquierda                               -> 0000 0010 1110    -<<4- 0010 1110
    uint16_t c = dieciseis<<12; // deplazas 4 hacia izquierda 7500 = 0000 0010 1110 1110    -> 0000 0010 1110 1110 -<<12- 1100
    // concateno c b y a.
    // concat ->  es como decir: mi primer grupo (menos significativo) es a, y el segundo grupo (mas significativo) es b.
    uint16_t concat = c|b|a;
    return(concat);
}
// MUY IMPORTANTE!!!!!
// unsigned char: Es el tipo básico de C. Casi siempre tiene 8 bits (1 byte). Solo puede almacenar valores de 0 a 255.
// uint16_t: Es un tipo de dato de la librería <stdint.h>. El "16" significa que tiene exactamente 16 bits (2 bytes). Puede almacenar valores de 0 a 65,535.
//para swapear 8bits necesito un unsignet, para swapera 16 bits uint16_t

#include <stdio.h> 
int main()
{
    int a = 750;
    //a = 0000 0010 1110 1110
    printf("%b\n", a); 
    a=swap_bits(a); // es una posibilidad para swap, que los primeros 4 vayan al final y los ultimos al principio
    //a = 1110 0010 1110 0000
    printf("%b\n\n", a);
    return 0;
}