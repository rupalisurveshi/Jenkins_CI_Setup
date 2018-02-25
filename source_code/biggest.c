#include"header.h"

int main()
{
int i,j,k,b;
//printf("Enter i,j,k\n");
//scanf("%d%d%d",&i,&j,&k);

i = 10;
j = 20;
k = 15;

b = i>j ? i>k ? i : k : j>k ? j : k;

printf("i = %d\nj = %d\nk = %d\nb = %d\n",i,j,k,b);

endiancheck();
}
