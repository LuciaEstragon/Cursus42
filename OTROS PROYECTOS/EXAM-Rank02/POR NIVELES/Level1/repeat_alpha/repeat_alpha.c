 #include <unistd.h>

void ft_putstr(const char *s)
{
	int i = 0;
        while(s[i] != '\0')
        {
                write(1, &s[i], 1);
		i++;
        }
}

void ft_putstr_repeat(char *s)
{
        int i = 0;
	int repeat = 0;
        while(s[i] != '\0')
        {
		repeat = 0;
		if (s[i] >= 65 && s[i] <= 90)
			repeat = s[i] - 65;
		if (s[i] >= 97 && s[i] <= 122)
                        repeat = s[i] - 97;
		while(repeat >= 0)
		{
                	write(1, &s[i], 1);
			repeat --;
		}
		i++;
        }
}

//#include <stdio.h>
int main(int argc, char **argv)
{
	if (argc <= 1)
	{
		//write(1, "end1\n", 5);
		return 0;
	}
	char *str = argv[1];
	//ft_putstr(str);
	//printf("%s", str);
	//write(1, "stop\n", 5);
	ft_putstr_repeat(str);
	//write(1, "end2\n", 5);
	write(1, "\n", 1);
	//return (0);
}

/*
#include <unistd.h>

int main(int ac, char *av[])
{
    int i;
    int j;

    /* check the number of argument
     */
    if (ac == 2)
    {
        i = 0;
        /* loop over the whole string
         */
        while (av[1][i])
        {
            /* if the character is an upper-case letter
             */
            if (av[1][i] >= 65 && av[1][i] <= 90)
            {
                j = 0;
                /* loop while the j is smaller than the alphabetical
                 * index of the current character
                 * - 64 is to get the alphabetical index
                 * A in ASCII => 65, so 65 - 64 = 1
                 * Z in ASCII => 90, so 90 - 64 = 26
                 */
                while (j < av[1][i] - 64)
                {
                    write(1, &av[1][i], 1);
                    j++;
                }
            }
            else if (av[1][i] >= 97 && av[1][i] <= 122)
            {
                j = 0;
                /* loop while the j is smaller than the alphabetical
                 * index of the current character
                 * - 96 is to get the alphabetical index
                 * a in ASCII => 97, so 97 - 96 = 1
                 * z in ASCII => 122, so 122 - 96 = 26
                 */
                while (j < av[1][i] - 96)
                {
                    write(1, &av[1][i], 1);
                    j++;
                }
            }
            else
                /* if the current character is not a letter
                 * simply write the character
                 */
                write(1, &av[1][i], 1);
            i++;
        }
    }
    write(1, "\n", 1);
}*/
