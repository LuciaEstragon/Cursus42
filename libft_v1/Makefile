# Nombre del ejecutable
EXEC = lib
NAME = libft.a

# Compilador y sus flags
CC = cc 
CFLAGS = -Wall -Werror -Wextra

# Archivos fuente
SRCS = ft_isalpha.c ft_isdigit.c ft_isalnum.c ft_isascii.c ft_isprint.c ft_tolower.c ft_toupper.c \
	ft_strlen.c ft_strchr.c ft_strrchr.c ft_strlcpy.c ft_strnstr.c \
	ft_atoi.c ft_putnbr_fd.c  ft_putstr_fd.c  ft_putchar_fd.c \
	ft_memset.c 
	
OBJS = $(SRCS:.c=.o)
LIBS = unistd.h stddef.h libft.h

# Archivos de entrada
# FILES = dic.txt

# Regla por defecto
all: $(EXEC) lib

# Regla para compilar el ejecutable
$(EXEC): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(EXEC)

# Regla para compilar los archivos .c en .o
%.o: %.c $(LIBS)
	$(CC) $(CFLAGS) -c $<

# Regla para limpiar todo, incluyendo el ejecutable
clean:
	rm -f $(OBJS)
	
# Regla para limpiar los archivos objeto y el ejecutable
fclean: clean
	rm -f $(EXEC) $(NAME)

# Regla para leer los archivos y ejecutar el programa
run: $(EXEC)
	./$(EXEC) $(FILES)

# Regla para hacer una recompilacion (un re-make, como si se hubiera ejecutado Make por primera vez)
re: fclean all

lib:
	ar rcs $(NAME) $(OBJS)

nor:
	norminette -R CheckForbiddenSourceHeader

.PHONY: all clean fclean run re lib nor
