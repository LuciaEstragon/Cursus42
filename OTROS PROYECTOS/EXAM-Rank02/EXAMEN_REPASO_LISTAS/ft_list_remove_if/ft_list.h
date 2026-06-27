#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

typedef struct      s_list
{
    struct s_list   *next;
    void            *data;
}                   t_list;

