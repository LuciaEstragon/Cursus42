//Debe ordenar (in situ) el array int 'tab', que contiene exactamente los miembros 'size', en orden ascendente.
//Se deben conservar los dobles.


void sort_int_tab(int *tab, unsigned int size)
{
    int i=0;
    int v_max=0;
    int v_min=0;
    while(i<size)
    {
        if(tab[i]>=v_max)
            v_max = tab[i];
        if(tab[i]<=v_min)
            v_min = tab[i];
        i++;
    }
    i=0;
    int j=1;
    int temp;
    while(tab[i]!=v_min && tab[size]!=v_max)
    {
        while(j<=size)
        {
            if(tab[i]>=tab[j])
            {
                temp=tab[i];
                tab[i]=tab[j];
                tab[j]=temp;
            }
           j++;i++;
        }
    }


}

#include <unistd.h>
void putnbr(int i)
{
    if(i >= 10)
        putnbr(i/10);
    char c = (i%10)+'0';
    write(1, &c, 1);
}

int main()
{
    int tab[] = {2, 4, 5, 1, 2, 6};
    int size = 6;
    int i = 0;
    while(i<size)
    {
        putnbr(tab[i]);
        i++;
    }
    //sort_int_tab(*tab, size);
    write(1, "\n", 1);
    i=0;
    while(i<size)
    {
        putnbr(tab[i]);
        i++;
    }
    return 0;
}