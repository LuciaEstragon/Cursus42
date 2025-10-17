/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 10:31:57 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/02 10:34:20 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */



#include "libft.h"

int f_count_pal(char const *s, char c)
{
	int ind;
	int count_pal;
	int flag;

	ind = 0;
	count_pal = 0;
	flag = 0;
	while(s[ind] != '\0')
	{
		if(s[ind] != c && flag==0)
		{
			flag = 1;
			count_pal ++;
		}
		if(s[ind] == c && flag==1)
			flag = 0;
		ind++;
	}
	return(count_pal);
}

char **ft_split(char const *s, char c)
{
////funcion que cuenta palabras
	int count_pal;

	count_pal = f_count_pal(s, c);
////
	char dst1[10] = {0};
	const char *got;
	int len;
	char **result;
	int d_count=0;
	
	result = (char**)calloc(count_pal + 1, sizeof(char*));
		if(!result)
			return(0);
while(d_count < count_pal)
{
		got = ft_strchr(s, c);
		len = ft_strlen(s) - ft_strlen(got) + 1;
		ft_strlcpy(dst1, s, len);
		if (len > 1)
		{
			int i = 0;
			result[d_count] = (char*)malloc(ft_strlen(dst1) + 1);
			while (dst1[i] != '\0')
			{
				result[d_count][i] = dst1[i];
				i++;
			} 
			result[d_count][i+1] = '\0';
			d_count++;
		}
		if(d_count < count_pal)
		{
			got++;
			s = ft_strdup(got);
		}
}
	//result[d_count+1] = '\0';
	return(result);
}    

/*
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{	
		char *s = "hola..que..tal.";
		char c = '.';

		ft_split(s, c)
	printf("\n");
	int j=0, i;
	while(j < f_count_pal(s, c))
	{
		i = 0;
		 while (result[j][i] != '\0')
		 {
		printf("%c", result[j][i]);
		i++;
		 }
		 printf("\n");
		j++;
	}


	return 0;
}*/