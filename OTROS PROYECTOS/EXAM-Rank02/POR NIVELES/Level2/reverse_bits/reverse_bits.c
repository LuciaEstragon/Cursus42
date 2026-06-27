unsigned char	reverse_bits(unsigned char octet)
{
	unsigned int	i;
	unsigned char	res = 0;

	i = 8; //bit = 0001 1010
	while (i--)
	{
        res = (res << 1) | (octet & 1); 
        octet = octet >> 1;
	}
	return (res);
}
// BUCLE EXPLICADO
//bit = 0001 1010
    //res = 1  (res<<1 = 0 | bit&1 = 1)
//bit = 0001 101
    //res = 11  (res<<1 = 10 | bit&1 = 1)
//bit = 0001 10
    //res = 110  (res<<1 = 110 | bit&1 = 0)
//bit = 0001 1
    //res = 1100  (res<<1 = 1100 | bit&1 = 0)
//bit = 0001
    //res = 11001 (res<<1 = 11000 | bit&1 = 1)
//bit = 000
    //res = 110010  (res<<1 = 110010 | bit&1 = 0)
//bit = 00
    //res = 1100100  (res<<1 = 0 | bit&1 = 0)
//bit = 0
    //res = 11001000  (res<<1 = 0 | bit&1 = 0)


//entrada = 11010
// RESPUESTA REAL = 010110000 
/*#include<stdio.h>
int main()
{
    unsigned char bit = 13; 
    //bit = 0000 1101
      // bit << 1  -->  0001 1010 (move all izq)
      // bit >> 1  -->  0000 0110 (move all der)
    // (bit & 1) --> paridad (numero de 1) impar == 1, par = 0;
    // ((bit >> 1)|0) --> desplazo y el ultimo num es un 0  ==> 0000 1101 -->  0000 0110 (move all der)  ==> 0110
    // ((bit >> 1)|1) --> desplazo y el ultimo num es un 1                                              ==> 0111
    // ((bit << 1)|0) --> desplazo y el ultimo num es un 0  ==> 0000 1101 -->  0001 1010 (move all izq)  ==> 1 1010
    // ((bit << 1)|1) --> desplazo y el ultimo num es un 1                                              ==> 1 1011
    unsigned char rv_bit;
    printf("%b \n", bit<<1);
    rv_bit = reverse_bits(bit<<1);
    printf("%b \n", rv_bit);
    return 0;
}*/
