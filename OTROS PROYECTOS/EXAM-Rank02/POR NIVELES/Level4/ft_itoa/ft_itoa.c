// int to ascii //11:55
#include <unistd.h>

int len_dig(int n)
{
	int len = 0;
	while(n>=10) 
	{
		n=n/10;
		len++;
	}
	return(len+1);
}
char	*itoa(int nbr)
{
	int len = len_dig(nbr);
	char	*str = (char*)malloc(sizeof(char)*len+1);
	if (!str)
		return(NULL);
	str[len] = '\0';

	if(nbr == 0)
	{
		str[0] = '0';
		return(str);
	}

	return (str);
}

void putstr(char *s)
{
	int i=0;
	while(s[i])
	{
		write(1, &s[i], 1);
		i++;
	}
}

int	main(int argc, char **argv)
{
	if (argc !=2)
	{
		write(1, "\n", 1);
		return (0);
	}
	char *msg = argv[1];
	int nbr = 0;
	if(msg=="as") nbr=-12;
	putstr(itoa(nbr));
	write(1, "\n", 1);
	return (0);
}
