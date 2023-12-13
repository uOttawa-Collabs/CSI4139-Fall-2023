int printf(const char *fmt, ...);

void f(int *in , int *out) {
 long s[2] , local1 = 0;
 // Expansion phase
 s [0] = in [0] + 762;
 s [1] = in [0] | (9 << (s [0] % 16 | 1));
 // Mixing phase
 while ( local1 < 2) {
   s [1] |= (s [0] & 15) << 3;
   s[( local1 + 1) % 2] = s[ local1 ];
   local1 += 1;
 }
 if (s[0] > s [1]) {
  s [0] |= (s [1] & 31) << 3;
 } else {
  s [1] |= (s [0] & 15) << 3;
 }
 s [0] = s [1];
 // Compression phase
 out [0] = (s [0] << (s [1] % 8 | 1));
}

int main (int ac , char * av []) {
  int out ;

  f(av [1] , &out );
  if ( out == 0xa199abd8 ) /* "1234" -> 0xa199abd8 and "12345" also -> 0xa199abd8 */
    printf (" You win !\n");
  return 0;
}
