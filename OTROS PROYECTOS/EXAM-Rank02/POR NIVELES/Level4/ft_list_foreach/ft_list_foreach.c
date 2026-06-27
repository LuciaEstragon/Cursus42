
// MI PRIMER PROGRAMA CON LISTAS
// 1. crea un nodo
// 2. añade nodo a la lista
// 3. imprime la lista por pantalla
// (*). Liberar memoria - funciona sin hacerlo, pero es una mala practica
  //   (ESTE FREE ESTA RARO)

// EXAMEN ITERI !
// he recreado la forma de imprimir una lista, pasanto toda la lista por una funcion

#include <unistd.h>
#include <stdlib.h>

typedef struct	s_list
{
	struct s_list	*next;
	void			*data;
}	t_list;

// agrega un dato nuevo a la lista = un nuevo nodo
t_list	*list_new_dato(void *dato) // CREAR UN NODO //t_list	*ft_lstnew(void *content)
{
	t_list	*lista;

	lista = (t_list *)malloc(1 * sizeof(t_list));
	if (!lista)
		return (NULL);

	lista->data = dato;
	lista->next = NULL;

	return (lista);
}

// ese nodo nuevo se agrega a una lista creada - AL_FINAL
t_list	*list_add_al_final(t_list *lista, void *dato)
{
	t_list	*new_node;
	t_list	*lista__actualizar;

	// dato a agregar - nodo nuevo
	new_node = list_new_dato(dato);
	if (!new_node)
		return (NULL);

	// si no habia ninguna lista de antes y este es el primer nodo
	if (lista == NULL)
		return (new_node);

	// si si hay una lista -> avanzo todo el puntero next hasta el ultimo vagon
	lista__actualizar = lista;
	while (lista__actualizar->next != NULL)  // esto es lo mismo que list_len(lista) pero sin devolver nada
		lista__actualizar = lista__actualizar->next;

	// agrego mi nodo al final de la lista y me reenvio la lista de vuelta
	lista__actualizar->next = new_node;
	return (lista__actualizar);
}
//strlen version lista  // como avanzar en una lista
int list_len(t_list *lista) 
{
    int len = 0;
    while (lista->next)
    {
        lista = lista->next;
        len++;
    }
    return (len);
}
// ese nodo nuevo se agrega a una lista creada - AL_PRINCIPIO
t_list	*list_add_al_principio(t_list *lista, void *dato)
{
	t_list	*new_node;

	// dato a agregar - nodo nuevo
	new_node = list_new_dato(dato);
	if (!new_node)
		return (NULL);

	// tanto si existe como si no existe lista da igual porque este nodo nuevo siempre es el primero
	new_node->next = lista;
	return (new_node);
}

// Leer-imprimir la lista por pantalla
void	list_read(t_list *lista)
{
	t_list *lista_actual = lista;

	while (lista_actual)
	{
		char *str = (char *)lista_actual->data;
		int i = 0;
		while(str[i]) // esto es un putstr normal
		{
			write(1, &str[i], 1);
			i++;
		}
		write(1, " ", 1);
		lista_actual = lista_actual->next++;
	}
}

void putstr(void *str)
{
	char *s = str;
	int i=0;
	while(s[i]) // esto es un putstr normal
	{
		write(1, &s[i], 1);
		i++;
	}
}
//vamos a intentar pasar la lista por la funcion putstr
//esta funcion deberia hacer lo mismo que la funcion para leer anterior
void	ft_list_foreach(t_list *begin_list, void (*f)(void *)) //void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	if (!begin_list || !f)
		return ;
	while (begin_list)
	{
		(*f)(begin_list->data); // (*f)(list_ptr->data); //EXAMEN
		begin_list = begin_list->next;
	}
}


// Liberar memoria
void	list_free(t_list *lista)
{
	t_list	*current = lista;
	t_list	*next;

	while (current != NULL)
	{
		next = current->next;
		free(current);
		current = next;
	}
}
int	main()
{
	t_list *mi_lista = NULL;
	t_list *mi_lista_reverse = NULL;
	char *msg = "Lucia";
	char *msg2 = "Estrada";

	mi_lista = list_add_al_final(mi_lista, msg);
	mi_lista = list_add_al_final(mi_lista, msg2);
	//list_read(mi_lista);
	write(1, "FUNCION ITERI, del Examen\n", 26);
	ft_list_foreach(mi_lista, putstr);
	write(1, "\n", 1);
	mi_lista_reverse = list_add_al_principio(mi_lista_reverse, msg);
	mi_lista_reverse = list_add_al_principio(mi_lista_reverse, msg2);
	list_read(mi_lista_reverse);

	// Liberar memoria
	//list_free(mi_lista);
	return (0);
}
