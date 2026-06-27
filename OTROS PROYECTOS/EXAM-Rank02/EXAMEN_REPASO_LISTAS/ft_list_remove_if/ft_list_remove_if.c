#include "ft_list.h"

/*int (*cmp)()
{

}
void ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)())
{

}*/
void addNodo(t_list **miLista, t_list *newNodo)
{
    if(miLista == NULL)
        *miLista = newNodo;
    else
    {
        t_list *temp = *miLista;
        while(temp->next != NULL)
            temp = temp->next;
        temp->next = newNodo;
    }
}
void print(t_list **miLista)
{
    t_list *temp = *miLista;
    while(temp)
    { /*
        char *str = (char *)temp->data;
        int i=0;
        while(str[i])
        {
            write(1, &str[i], 1);
            i++;
        }*/
        printf("[%s] -> ", (char*)temp->data);
        temp = temp->next;
    }
}

void print_CORR(t_list **miLista)
{
    t_list *temp = *miLista;
    while (temp)
    {
        char *str = (char *)temp->data;
        write(1, "[", 1);
        write(1, str, strlen(str));
        write(1, "] -> ", 5);
        temp = temp->next;
    }
    write(1, "NULL\n", 5);
}
int main(int argc, char **argv)
{
    if(argc<2)
    {
        write(1, "end1", 4);
        return 0;
    }
    t_list *miLista;
    int i=1;
    while(argv[i] != NULL)
    {
        t_list *newNodo = malloc(sizeof(t_list));
        newNodo->next=NULL;
        newNodo->data=argv[i];
        addNodo(&miLista, newNodo);
        i++;
    }
    print_CORR(&miLista);
    write(1, "end2", 4);
    return 0;
}