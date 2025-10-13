/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lestrada <lestrada>                        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/01 13:45:33 by lestrada          #+#    #+#             */
/*   Updated: 2025/10/01 17:19:44 by lestrada         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_IS_H
# define LIBFT_IS_H

#include <unistd.h>
#include <stddef.h>

int	ft_isdigit(int c);
int	ft_isalpha(int c);
int	ft_isalnum(int c);
int	ft_isascii(int c);
int	ft_isprint(int c);
int	ft_toupper(int c);
int	ft_tolower(int c);
size_t	ft_strlen(const char *str);
char    *ft_strchr(const char *str, int c);
char    *ft_strrchr(const char *str, int c);

#endif
