/* Credit: 
https://axcheron.github.io/playing-with-ld_preload/ 
*/

#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>
#include <string.h>

int (*real_strcmp)(const char *str1, const char *str2);

int strcmp(const char *str1, const char *str2) {

  if(!real_strcmp) real_strcmp = dlsym(RTLD_NEXT, "strcmp");

  printf("str1 = '%s' and ", str1);

  printf("str2 is '%s' \n", str2);
  return real_strcmp(str1,str2);
}
