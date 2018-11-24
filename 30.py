#include <stdio.h>
 
int main(void)
{
	int s,p1,r,q,a,a2,t,n1,n2;
	scanf("%d%d",&s,&p1);
	scanf("%d%d",&r,&q);
	a=s*60+p1;
	a2=r*60+q;
	if(a>a2)
	{
		t=a-a2;
		n1=t/60;
		n2=t%60;
		printf("%d %d",n1,n2);
	}
	else
	{
		t=a2-a;
		n1=t/60;
		n2=t%60;
		printf("%d %d",n1,n2);
	}
}		
 
 
