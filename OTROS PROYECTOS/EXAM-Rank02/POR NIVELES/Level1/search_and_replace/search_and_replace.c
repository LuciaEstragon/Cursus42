#include<unistd.h>

int ft_strlen(char *s)
{
	int i = 0;
	while (s[i] != 0)
		i++;
	return (i);
}

void ft_putstr(char *s)
{
	int i = 0;
	while(s[i] != 0)
	{
		write(1, &s[i], 1);
		i++;
	}
}

char *ft_find(char *msg, char *sust1, char *sust2)
{
	int i = 0;
	char s = sust1[0];
	char r = sust2[0];

	while (msg[i] != 0)
	{
		if(msg[i] == s)
			msg[i] = r;
		i++;
	}
	return (msg);

}

int main(int argc, char **argv)
{
	if (argc != 4)
		write(1, "\n", 1);
	char *msg = argv[1]; 
	char *sust1 = argv[2];
	char *sust2 = argv[3];

	int a = ft_strlen(sust1);
	int b = ft_strlen(sust2);	
	if(a>1 || b>1)
		write(1, "\n", 1);

	//ft_putstr(msg);
	
	ft_find(msg, sust1, sust2);
	ft_putstr(msg);

	//return 0;
	write(1, "\n", 1);
}

