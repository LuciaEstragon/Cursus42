#include<stdio.h>
#include<stdlib.h>
#include<string.h>


void compare(char const *s1, char const *set, int *i, int *j)
{
	int flag = 0;
	while(s1[i] == set[j])
	{
		i++;
		j++;
		if(set[j] == '\0')
			flag = 1;
	}
	if (flag == 1)
	{
		flag = 0;
		j = 0;
	}
}

char *ft_strtrim(char const *s1, char const *set)
{
	char *ptr;

	ptr = (char*)malloc(strlen(s1));
	if(!ptr)
		return(NULL);

	int	i=0, j=0, k=0;
	while (s1[i] != '\0')
	{
		if(s1[i] == set[j])
		{
			compare(s1, set, &i, &j);
			/*while(s1[i] == set[j])
			{
				i++;
				j++;
				if(set[j] == '\0')
					flag = 1;
			}
			if (flag == 1)
			{			
				flag = 0;
				j = 0;
			}*/			
			while (j != 0)
			{
				ptr[k]=s1[i-j];
					j--;
					k++;
			}
		}
		else
		{
			ptr[k] = s1[i];
		i++;
		k++;
		}
	}
	return (ptr);
}

int	main(void)
{
        char* msg;
        msg = "hola, que tal? que ase quien?";
        char *set;
	char* ptr;

	set = "q";
	ptr = ft_strtrim(msg, set);
	printf("%s",ptr);
	set = "que";
	ptr = ft_strtrim(msg, set);
        printf("%s",ptr);

	return(0);
}
