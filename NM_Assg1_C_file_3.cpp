#include<iostream>
#include<conio.h>
#include<stdlib.h>

using namespace std;

int main()
{
	
	//Part 1
	float* x = (float*)malloc(100*sizeof(float));
	float* y;
	float* fun(float* a,int m);
	cout<<" \n The elements of the array assigned using malloc are \n";
	for(int i=1;i<=100;i++)
	{
		x[i]=i*i;
		cout<<"\t"<<x[i];
		if (i%10==0)
			cout<<"\n";	
	}
	
	//Part 2
	y= fun(x,100);
	cout<<"\n The mean of this distribution is : "<<y[0]<<" and the variance is : "<<y[1];
	free(x);
	free(y);
	getch();
	return 0;
}
float* fun(float* a,int m)
{
	float* y=(float*)malloc(2*sizeof(float));
	//loop for calculating mean
	for(int i=1;i<=m;i++)
	{
		y[0]+=a[i];
	}
	y[0]/=m;
	
	//loop for calculating variance
	for(int i=1;i<=m-1;i++)
	{
		y[1]+=(y[0]-a[i])*(y[0]-a[i]);
	}
	y[1]/=m;
	return y;
}
