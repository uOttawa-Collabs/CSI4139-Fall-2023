#include <stdio.h>

int initialized_variable = 42;
int uninitialized_variable;

int main(void) {
    printf("Initialized variable: %d\n", initialized_variable);
    printf("Uninitialized variable: %d\n", uninitialized_variable);
    return 0;
}
