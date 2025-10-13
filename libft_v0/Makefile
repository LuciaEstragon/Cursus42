# Nombre del ejecutable
EXEC = lib
NAME = libft.a

# Compilador y sus flags
CC = cc 
CFLAGS = -Wall -Werror -Wextra

# Archivos fuente
SRCS = ft_isalpha.c ft_isdigit.c ft_isalnum.c ft_isascii.c ft_isprint.c ft_tolower.c ft_toupper.c ft_strlen.c ft_strchr.c ft_strrchr.c
OBJS = $(SRCS:.c=.o)

# Archivos de entrada
# FILES = dic.txt

# Regla por defecto
all: $(EXEC) lib

# Regla para compilar el ejecutable
$(EXEC): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(EXEC)

# Regla para compilar los archivos .c en .o
%.o: %.c unistd.h libft.h
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
	norminette -R check

.PHONY: all clean fclean run re lib nor
