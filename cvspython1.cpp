#include<iostream>
#include<stdio.h>
#include<time.h>

using namespace std;

int main()
{
	int n;
	long long int fact;
	clock_t start_time,end_time;
	double time;
	start:
	// Taking input
	cout<<" \n Enter your number : ";
	cin>>n;
	// Checking for invalid input
	if (n<1)
	{
		cout<<" \n INVALID ";
		goto start;
	}
	long long int factorial(long long int m);
	
	//Calculating time for the operation
	start_time=clock();
	fact=factorial(n);
	end_time=clock();
	time=(double)((end_time-start_time)/CLOCKS_PER_SEC);
	
	cout<<" \n The Factorial is : "<<fact;
	printf(" \n Time taken for operation : %.7f ",time);
	return 0;
}
// Recursive function for calculating factorial
long long int factorial(long long int n)
{
	if (n<=1)
		return 1;
	else 
		return n*factorial(n-1);
	
}

