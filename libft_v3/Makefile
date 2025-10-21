# Nombre del ejecutable
EXEC = lib
NAME = libft.a

# Compilador y sus flags
CC = cc 
CFLAGS = -Wall -Werror -Wextra

RM   = rm -f

# Archivos fuente
SRCS = ft_isalpha.c ft_isdigit.c ft_isalnum.c ft_isascii.c ft_isprint.c ft_tolower.c ft_toupper.c \
	ft_strlen.c ft_strchr.c ft_strrchr.c ft_strlcpy.c ft_strnstr.c ft_strlcat.c ft_strncmp.c \
	ft_memset.c ft_bzero.c ft_memmove.c ft_memchr.c ft_memcmp.c ft_memcpy.c\
	ft_atoi.c ft_itoa.c ft_putnbr_fd.c ft_putstr_fd.c ft_putendl_fd.c ft_putchar_fd.c \
	ft_strjoin.c ft_substr.c ft_calloc.c ft_strdup.c ft_strtrim.c ft_split.c ft_striteri.c ft_strmapi.c

OBJS = $(SRCS:.c=.o)
LIBS = unistd.h stddef.h libft.h

# Archivos de entrada
# FILES = dic.txt

# Regla por defecto
all: $(NAME)

$(NAME): $(OBJS)
	ar rcs $(NAME) $(OBJS)

# Regla para compilar el ejecutable
$(EXEC): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(EXEC)

# Regla para compilar los archivos .c en .o
%.o: %.c $(LIBS)
	$(CC) $(CFLAGS) -c $<

# Regla para limpiar todo, incluyendo el ejecutable
clean:
	$(RM) $(OBJS)
	
# Regla para limpiar los archivos objeto y el ejecutable
fclean: clean
	$(RM) $(EXEC) $(NAME)

# Regla para leer los archivos y ejecutar el programa
run: $(EXEC)
	./$(EXEC) $(FILES)

# Regla para hacer una recompilacion (un re-make, como si se hubiera ejecutado Make por primera vez)
re: fclean all

nor:
	norminette -R CheckForbiddenSourceHeader

.PHONY: all clean fclean run re nor
