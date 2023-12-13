all: check strcmp_hook
	LD_PRELOAD="./strcmp_hook.so" ./check 5542

check: ex1.o checkpw.o
	gcc -o check checkpw.o ex1.o
ex1.o: ex1.c
	gcc -c ex1.c
checkpw.o: checkpw.c
	gcc -c checkpw.c
strcmp_hook: strcmp_hook.c
	gcc strcmp_hook.c -o strcmp_hook.so -fPIC -shared -ldl		
clean:
	rm *.so *.o check
correctpw:
	LD_PRELOAD="./strcmp_hook.so" ./check 123
		
