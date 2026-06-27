//INIT 9:50
//FIN 9:55
//TRY 1

#include <unistd.h>
#include "ft_list.h"


int	ft_list_size(t_list *begin_list)
{
    int len=1;
    while(begin_list->next != NULL)
    {
        begin_list=begin_list->next;
        len++;
    }
    return len;
}