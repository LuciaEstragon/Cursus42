#include <stdio.h>
#include <unistd.h>

void putstr(char* str)
{
    int i = 0;
    while(str[i])
    {
        write(1, &str[i], 1);
        i++;
    }
}

int hide(char* a, char*b)
{
    int i = 0;
    int j = 0;
    while(b[i])
    {
        if(b[i] == a[j])
            j++;
        if(a[j]=='\0')
            return 1;
        
        i++;
    }
    return 0;
}
int main(int argc, char** argv)
{
    if(argc!=3)
    {
        write(1, "\n",1);
        return 0;
    }
    char *msg1 = argv[1];
    char *msg2 = argv[2];
    // putstr(msg1);
    // write(1, "\n",1);
    // putstr(msg2);
    // write(1, "\n",1);
    // printf("msg1: %s, msg2: %s \n \n", msg1, msg2);
    int res = hide(msg1, msg2);
    char c_res = res + '0';
     write(1, &c_res,1);
     write(1, "\n",1);
    return 0;
}