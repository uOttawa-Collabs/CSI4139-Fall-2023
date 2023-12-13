#include <string.h>

int printf(const char *fmt, ...);

int main (int ac , char * av []) 
{
 char* psw = "1234";
 if(strcmp(av[1], psw)==0)
 {
   printf (" You win !\n");
 }
 return 0;
}

