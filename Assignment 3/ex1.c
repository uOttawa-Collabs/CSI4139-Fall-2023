#include <string.h>

int printf(const char *fmt, ...);

int checkpw(const char * str1, const char * str2);
 
int main (int ac , char * av []) 
{
 char* psw = "123";
 if (checkpw (av[1], psw))
 //if(strcmp(av[1], psw)==0)
 {
   printf (" You win !\n");
 }
 return 0;
}

