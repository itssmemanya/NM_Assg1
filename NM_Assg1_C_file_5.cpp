#include<iostream>
#include<conio.h>
#include<stdlib.h>
#include<C:\Users\HP\Documents\NM_Assg1_H_file_4.h>

using namespace std;

int main()
{
	
	//Part 1
	float* x = (float*)malloc(100*sizeof(float));
	float* y;
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
