/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 10:31:57 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/23 15:47:38 by lestrada         ###   ########.fr       */
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

static char		*fill_word(char const *s, char c, size_t *ind_s);
static size_t	count_words(char const *s, char c);
static char		*free_split(char **split, size_t size);

char	**ft_split(char const *s, char c)
{
	char	**result;
	size_t	total_word;
	size_t	ind_words;
	size_t	ind_s;

	if (!s)
		return (NULL);
	total_word = count_words(s, c);
	result = (char **)ft_calloc(total_word + 1, sizeof(char *));
	if (!result)
		return (NULL);
	ind_words = 0;
	ind_s = 0;
	while (ind_words < total_word)
	{
		while (s[ind_s] == c)
			ind_s++;
		if (s[ind_s] != '\0')
		{
			result[ind_words] = fill_word(s, c, &ind_s);
			if (!result[ind_words++])
				return (free_split(result, ind_words), NULL);
		}
	}
	return (result);
}

static char	*free_split(char **split, size_t size)
{
	while (size-- > 0)
		free(split[size]);
	free(split);
	return (NULL);
}

static size_t	count_words(char const *s, char c)
{
	size_t	ind;
	size_t	count;
	size_t	flag;

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

static char	*fill_word(char const *s, char c, size_t *ind_s)
{
	size_t	len_word;
	char	*word;
	size_t	start;

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
