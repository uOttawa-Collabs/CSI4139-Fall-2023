#include <string.h>

int checkpw(const char * str1, const char * str2)
{
 if(strcmp(str1, str2))
 {
  return 0; 
 }
 else
 {
  return 1; 
 }
}
 
