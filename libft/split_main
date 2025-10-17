

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    /* subtest 1: basic search */
    
        char *s = "hola..que..tal.";
        char c = '.';


////funcion que cuenta palabras
        int ind =0;
        int count_pal=0, flag=0;
        while(s[ind] != '\0')
        {

            if(s[ind] != c && flag==0)
            {
                flag = 1;
                count_pal ++;
            }
            if(s[ind] == c && flag==1)
                flag = 0;
            ind++;
        }
        printf("count palabras: %d", count_pal);

////
    char dst1[10] = {0};
    char *dst2;
    const char *got;
    size_t exp;
    int len;
    char **result;
    int count, d_count=0;
    
    result = (char**)calloc(count + 1, sizeof(char*));
        if(!result)
        {
            printf("NO he podido crear nada");
            return(0);
        }
while(d_count < count_pal)
{
        got = strchr(s, c);
        printf("got: %s", got);

        len = strlen(s) - strlen(got) +1;
        printf("len: %d", len);
        
        exp = strlcpy(dst1, s, len);
        printf("dst1: %s \n", dst1);
       
        //trlcat(result, dst1, len+strlen(result));
        if (len > 1)
        {
        
            //d_count++;
            int i = 0;
            result[d_count] = (char*)malloc(strlen(dst1) + 1);
            while (dst1[i] != '\0')
		    {
		        printf("dst1: %c  ", dst1[i]);
			    result[d_count][i] = dst1[i];
			    
			    i++;
			    
		    } 
		    result[d_count][i+1] = '\0';
		    d_count++;
        }
        if(d_count < count_pal){
    got++;
    s = strdup(got);}
}
    //result[count+1] = '\0';
    
    printf("\n");
    int j=0, i;
    while(j < count_pal)
    {
        i = 0;
         while (result[j][i] != '\0')
         {
        printf("%c", result[j][i]);
        i++;
         }
         printf("\n");
        j++;
    }


    return 0;
}
