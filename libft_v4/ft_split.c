/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 10:31:57 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/21 11:29:56 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
* Example usage: s= "..Hello....w.o.r  .ld..all"
* ft_split will create a string **result=[Hello][w][o][r  ][ld][all]
*
* 1º Count the number of words with count_words(), a method that finds edges.
* 2º Loop to fill each word with its letters. 
*
* Since it's a double pointer, you need two mallocs and free memory
*/

char	*fill_word(char const *s, char c, int *ind_s);
int		count_words(char const *s, char c);
char	*free_split(char **split, int size);

char	**ft_split(char const *s, char c)
{
	char	**result;
	int		total_word;
	int		ind_words;
	int		ind_s;

	total_word = count_words(s, c);
	result = (char **)ft_calloc(total_word + 1, sizeof(char *));
	if (!result)
		return (NULL);
	ind_words = 0;
	ind_s = 0;
	while (ind_words < total_word && s[ind_s])
	{
		while (s[ind_s] == c)
			ind_s++;
		if (s[ind_s] != '\0')
		{
			result[ind_words] = fill_word(s, c, &ind_s);
			if (!result[ind_words])
				return (free_split(result, ind_words), NULL);
			ind_words++;
		}
	}
	return (result);
}

char	*free_split(char **split, int size)
{
	while (size-- > 0)
		free(split[size]);
	free(split);
	return (NULL);
}

int	count_words(char const *s, char c)
{
	int	ind;
	int	count;
	int	flag;

	ind = 0;
	count = 0;
	flag = 0;
	while (s[ind] != '\0')
	{
		if (s[ind] != c && flag == 0)
		{
			flag = 1;
			count++;
		}
		else if (s[ind] == c && flag == 1)
			flag = 0;
		ind++;
	}
	return (count);
}

char	*fill_word(char const *s, char c, int *ind_s)
{
	int		len_word;
	char	*word;
	int		start;

	start = *ind_s;
	len_word = 0;
	while (s[start + len_word] != c && s[start + len_word] != '\0')
		len_word++;
	word = (char *)ft_calloc(len_word + 1, sizeof(char));
	if (!word)
		return (NULL);
	ft_strlcpy(word, &s[start], len_word + 1);
	*ind_s = start + len_word;
	return (word);
}
