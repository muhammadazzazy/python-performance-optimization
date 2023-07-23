// c -fPIC -shared -o libtest.so function.c
#include <stdio.h>

void f() {
	float total = 0;
	for(int i = 0; i < 5000; i++) {
		for(int j = 0; j < 5000; j++) {
			float z = i * j;
			total = total + z;
			printf("%f\n",z);
		}
	}
	printf("%f\n",total);
}