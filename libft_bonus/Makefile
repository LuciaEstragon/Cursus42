EXEC = lib
NAME = libft.a

CC = cc 
CFLAGS = -Wall -Werror -Wextra

RM   = rm -f

SRCS = ft_isalpha.c ft_isdigit.c ft_isalnum.c ft_isascii.c ft_isprint.c ft_tolower.c ft_toupper.c \
	ft_strlen.c ft_strchr.c ft_strrchr.c ft_strnstr.c ft_strlcat.c ft_strlcpy.c ft_strncmp.c \
	ft_memset.c ft_bzero.c ft_memmove.c ft_memchr.c ft_memcmp.c ft_memcpy.c\
	ft_atoi.c ft_itoa.c ft_putnbr_fd.c ft_putstr_fd.c ft_putendl_fd.c ft_putchar_fd.c \
	ft_strjoin.c ft_substr.c ft_calloc.c ft_strdup.c ft_strtrim.c ft_split.c ft_striteri.c ft_strmapi.c

SRCS_BONUS = ft_lstnew.c ft_lstadd_front.c ft_lstsize.c ft_lstlast.c ft_lstadd_back.c \
	ft_lstdelone.c ft_lstclear.c ft_lstiter.c ft_lstmap.c

OBJS = $(SRCS:.c=.o)
BONUS_OBJ = $(SRCS_BONUS:.c=.o)
LIBS = unistd.h stddef.h libft.h

# Archivos de entrada
# FILES = dic.txt

# Regla por defecto
all: $(NAME)

$(NAME): $(OBJS)
	ar rcs $(NAME) $(OBJS)

bonus: $(NAME) $(BONUS_OBJ)
	ar rcs $(NAME) $(BONUS_OBJ)

# Regla para compilar el ejecutable
$(EXEC): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(EXEC)

$(EXEC): $(BONUS_OBJ)
	$(CC) $(CFLAGS) $(BONUS_OBJ) -o $(EXEC)

# Regla para compilar los archivos .c en .o
%.o: %.c $(LIBS)
	$(CC) $(CFLAGS) -c $<

# Regla para limpiar todo, incluyendo el ejecutable
clean:
	$(RM) $(OBJS) $(BONUS_OBJ)
	
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

.PHONY: all clean fclean run re nor bonus
