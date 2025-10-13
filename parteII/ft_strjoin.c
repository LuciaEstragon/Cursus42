#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char *ft_strjoin(char const *s1, char const *s2)
{
	char	*ptr;
	size_t	ind;

	ptr = (char*)malloc(strlen(s1)+strlen(s2));
	if (!ptr)
		return(NULL);

	ind = 0;
	//if(s1!=NULL) {
	while(*s1 != '\0')
	{
		ptr[ind] = *s1;
		ind++;
		s1++;
	}//}
	//if(s2!=NULL){
	char *a=NULL;
	if(a==NULL) return(ptr);
	while(*s2 != '\0')
	{
		ptr[ind] = *s2;
		ind++;
		s2++;
	}//}
	return(ptr);
}

int	main(void)
{
	char	*msg;
	char	*ans;
	char	*msg_comp;
	
	msg = "Hola, que tal? \n";
	ans = NULL;
	msg_comp = ft_strjoin(msg, ans);
	printf("%s", msg_comp);
	ans = "Bien, gracias";
        msg_comp = ft_strjoin(msg, ans);
        printf("%s", msg_comp);
	return(0);
}
