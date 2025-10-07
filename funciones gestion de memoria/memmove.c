/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   memmove.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 10:53:55 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/07 19:11:09 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	dirr_mem(void *ptr1, void *ptr2)
{
	if(ptr1 == ptr2)
		return (0);
	else if(ptr1 < ptr2)
		return (1);
	else
		return (2);
}
/*
 * Que dirreccion de memoria (dirr_mem) ocupan estos punteros:    
   return 0 = ocupan la misma direccion de memoria
   return 1 = ptr1 esta antes que dos
   return 2 = ptr2 esta despues que uno


  // Para punteros del mismo tipo, podemos comparar contenido
    if(ptr1 && ptr2) { // Solo si no son NULL
        printf("→ Ambos punteros son válidos (no NULL)\n");
    }
*/
