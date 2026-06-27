#include <stdlib.h>
#include <stdio.h>

typedef struct      s_list
{
    struct s_list   *next;
    void            *data;
}                   t_list;

void addNodo(t_list **miLista, t_list *newNodo)
{
    if (*miLista == NULL)
        *miLista = newNodo;
    else
    {
        t_list *temp = *miLista;
        while (temp->next != NULL)
            temp = temp->next;
        temp->next = newNodo;
    }
}

void print(t_list *miLista)
{
    t_list *temp = miLista;
    while (temp)
    {
        printf("[%s] -> ", (char*)temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

void freeList(t_list *miLista)
{
    t_list *temp;
    while (miLista)
    {
        temp = miLista;
        miLista = miLista->next;
        free(temp);
    }
}

int main(int argc, char **argv)
{
    if (argc < 2)
    {
        printf("No hay argumentos.\n");
        return 0;
    }

    t_list *miLista = NULL;
    int i = 1;
    while (argv[i] != NULL)
    {
        t_list *newNodo = malloc(sizeof(t_list));
        if (!newNodo)
        {
            perror("malloc");
            freeList(miLista);
            return 1;
        }
        newNodo->next = NULL;
        newNodo->data = argv[i];
        addNodo(&miLista, newNodo);
        i++;
    }

    print(miLista);
    freeList(miLista);
    return 0;
}