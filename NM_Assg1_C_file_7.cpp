#include<iostream>
#include<conio.h>
#include<stdlib.h>

using namespace std;

int main()
{
	
	//Part 1
	float* x = (float*)calloc(100,sizeof(float));
	
	cout<<" \n The elements of the array before assignment using calloc are \n";
	for(int i=1;i<=100;i++)
	{
		cout<<"\t"<<x[i];
		if (i%10==0)
			cout<<"\n";	
	}
	
	cout<<" \n The elements of the array assigned using malloc are \n";
	for(int i=1;i<=100;i++)
	{
		x[i]=i*i;
		cout<<"\t"<<x[i];
		if (i%10==0)
			cout<<"\n";	
	}

	free(x);
	getch();
	return 0;
}
