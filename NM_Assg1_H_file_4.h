#include<iostream>
#include<conio.h>
#include<stdlib.h>

using namespace std;
float* fun(float* a,int m);
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
