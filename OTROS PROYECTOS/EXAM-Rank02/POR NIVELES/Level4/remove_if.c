//rev listas
#include<unistd.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>

typedef struct    s_list
{
    struct s_list *next;
    void          *data;
} t_list;


t_list *new(void* data)
{
    t_list *nodo=(t_list *)malloc(sizeof(t_list *));
    nodo->data = data;
    nodo->next = NULL;
    return (nodo);
}

void add(t_list **lista, void* data)
{
    t_list *nodo=new(data);
    t_list *temp=*lista;
    if(*lista==NULL)
        *lista = nodo;
    else
    {
        while(temp->next != NULL)
            temp=temp->next;
        temp->next=nodo;
    }
}

void print(t_list *lista)
{
    int i=0;
    while(lista)
    {
        printf("[%s]", (char*)lista->data);
        lista=lista->next;
    }
}

/////////////////////////////////////////////////////////////////////////////////////////////////////

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] != '\0' || s2[i] != '\0')
	{
        printf("HOLA %c . %c", s1[i], s2[i]);
		if (s1[i] != s2[i])
        {
            printf("No");
			return (s1[i] - s2[i]);
        }
		i++;
	}
	return (0);
}

int cmp(void *a, void *b) //NO USAR
{
    char *aa = a;
    char *bb = a;

    int res=ft_strcmp(a, b);
    //int res=ft_strcmp(aa, bb);
    //int res=strcmp(aa, bb);
    return (res);

}
/////////////////////////////////////////////////////////////////////////////////////////////////////

void delete(t_list **begin_list, void *data_ref)
{
    t_list *temp = *begin_list;
    t_list *siguiente = temp->next;

    /*if(temp->data == data_ref)
    {
        *begin_list = temp->next;
        free(temp);
    }
    else
    {
        if(siguiente->data == data_ref)
        {
            if(siguiente->next != NULL)
                temp->next = NULL;
            else
            {
                temp->next = siguiente->next;
                temp=siguiente;
                siguiente = temp->next;
            }
        }
        else
        {
            temp=siguiente;
            siguiente = temp->next;

        }

    }*/
    //if(*temp == *begin_list)
    while(begin_list)
    {
    if (temp->data == data_ref)
    {         // El nodo a borrar es el primero
            *begin_list = temp->next;
            temp = *begin_list;
    }
    if  (siguiente->data == data_ref)                    // El nodo está en medio o al final
    {
        temp->next = siguiente->next;
        temp=siguiente;
        siguiente = temp->next;
        //free(temp);            // Liberamos solo la estructura del nodo
    }
    }
}




// tarea 0 - main de listas con las funciones new--add-print -> 15min
// tarea expecifica 1 - compare
// tarea expecifica 2 - delete
int main() 
{
    t_list *mi_lista = NULL;
    add(&mi_lista, "hoola");
    add(&mi_lista, "qe");
    add(&mi_lista, "hoola");
    add(&mi_lista, "qe");
    add(&mi_lista, "tal");

    print(mi_lista);
    printf("\n");

    //tarea especifica
    /*void *a = "bbb";
    void *b = "aaa";
    printf("%d",cmp(a, b));
    printf("%d", ft_strcmp(a, b));*/

    //tarea especifica
    //delete(&mi_lista, "hoola");
    delete(&mi_lista, "qe");
    print(mi_lista);


    return (0);
}


 //NOTA MUY CONFUSO - compare
 //- no cambiar de void a char, usar directamente la funcion strcmp, metiendole numeros datos void
 //si usas cmp para cambiar a char no hace el compare