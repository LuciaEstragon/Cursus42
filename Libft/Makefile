# Nombre del ejecutable
EXEC = lib

# Compilador y sus flags
CC = gcc 
CFLAGS = -Wall -Werror -Wextra

# Archivos fuente
SRCS = main.c ft_isalpha.c ft_isdigit.c #ft_isalnum.c
OBJS = $(SRCS:.c=.o)

# Archivos de entrada
# FILES = none.txt

# Regla por defecto
all: $(EXEC)

# Regla para compilar el ejecutable
$(EXEC): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(EXEC)

# Regla para compilar los archivos .c en .o
%.o: %.c unistd.h
	$(CC) $(CFLAGS) -c $<

# Regla para limpiar todo, incluyendo el ejecutable
clean:
	rm -f $(OBJS)
	
# Regla para limpiar los archivos objeto y el ejecutable
fclean: $(clean)
	rm -f $(EXEC)

# Regla para leer los archivos y ejecutar el programa
run: $(EXEC)
	./$(EXEC) $(FILES)

# Regla para hacer una recompilacion (un re-make, como si se hubiera ejecutado Make por primera vez)
re: fclean all

lib:
	ar rcs libft.a ft_isalpha.o ft_isdigit.o

.PHONY: all clean fclean run re lib
