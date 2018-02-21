#include<stdio.h>
void main()
{
int i = 1 ;
char *p = &i;
if (*p == 1)
printf("little endian\n");
else
printf("big endian\n");

p++;

printf("%d\n",*p);

}

