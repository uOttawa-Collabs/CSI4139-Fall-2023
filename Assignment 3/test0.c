int printf(const char *fmt, ...);

void f(int *in , int *out) {
 long s[1];
 s [0] = in [0];
 out [0] = s [0];
}

int main (int ac , char * av []) {
  int out ;

  int *as_int =(int *) av[1];
  f(as_int , &out );
  if (out == 0x34333231) /* ASCII version of 1234 */
    printf (" You win !\n");
  return 0;
}
