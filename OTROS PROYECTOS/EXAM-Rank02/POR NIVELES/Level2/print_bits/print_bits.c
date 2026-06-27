//INIT:9:10
//END:9:50
//TRY:1


char *copy(char* dest, char* origen)
{
    int i=0;
    while(origen[i] != '\0')
    {
        dest[i]= origen[i];
        i++;
    }
    dest[i]='\0';
    return dest;
}

#include<unistd.h>
#include<stdio.h>
void	print_bits(unsigned char octet)
{
    int bit;
    char c_bit;
    int i=7;
    while(i>=0)
    {
        bit = (octet>>i)&1;
        c_bit=bit+'0';
        //printf("%d",(octet>>i)&1 );
        i--;
        write(1, &c_bit, 1);
    }
}/*
int main()
{
    print_bits(2);
    return 0;
}*/
/*void	print_bits(unsigned char octet)
{
    int bit[8];
    int i=0;
    while(octet>=2)
    {
        bit[i]=octet%2;
        octet=octet/2;
        i++;
    }
    bit[i]=octet;

    i=8;
    char c_bit;
    while(i>0)
    {
        c_bit = bit[i]+'0';
        write(1, &c_bit, 1);
        i--;
    }
}*/
