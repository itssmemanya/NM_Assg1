#include<iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "gsl_statistics.h"
#include<C:\Users\HP\Documents\NM_Assg1_H_file_4.h>

using namespace std;

int main() 
{
    //Part 1
    float *x = (float *)calloc(100 ,sizeof(float)); 
	for(int i=1;i<=100;i++)
		x[i]=i*i;
    float *y = fun(x, 100); 
    cout<<" \n Using function built by me : ";
    cout<<" \n The mean of this distribution is : "<<y[0]<<" and the variance is : "<<y[1];

    //Part 2
    float mean = gsl_stats_mean(x, 1, 100);
    float variance = gsl_stats_variance(x, 1, 100);

    cout<<" \n Using GSL functions : ";
    cout<<" \n The mean of this distribution is : "<<mean<<" and the variance is : "<<variance;

    // Freeing the memory used for the array
	free(x);
	free(y);
	getch();
	return 0;
}

