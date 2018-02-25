#include"header.h"

void endiancheck()
{
int i = 1 ;
char *p = (char*)&i ;
if (*p == 1)
printf("little endian\n");
else
printf("big endian\n");
}

