#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "libft.h"

void	print_content(void *content)
{
	printf("%s\n", (char *)content);
}

void	free_content(void *content)
{
	free(content);
}

int	main(void)
{
	t_list	*list;

	list = ft_lstnew(ft_strdup("Hello"));
	ft_lstadd_back(&list, ft_lstnew(ft_strdup("World")));
	ft_lstadd_back(&list, ft_lstnew(ft_strdup("From")));
	ft_lstadd_back(&list, ft_lstnew(ft_strdup("Linked")));
	ft_lstadd_back(&list, ft_lstnew(ft_strdup("List")));

	printf("Contenido de la lista:\n");
	ft_lstiter(list, print_content);
	printf("\nTamaño de la lista: %d\n", ft_lstsize(list));

	t_list	*last;

	last = ft_lstlast(list);
	if (last)
		printf("Último elemento: %s\n", (char *)last->content);

	ft_lstclear(&list, free_content);

	if (!list)
		printf("\nLista liberada correctamente (lista = NULL)\n");

	return (0);
}