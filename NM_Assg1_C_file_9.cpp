#include<iostream>
#include<fstream>
#include<conio.h>
#include<stdlib.h>
#include<C:\Users\HP\Documents\NM_Assg1_H_file_4.h>

using namespace std;

int main()
{
	
	//Part 1
	float* x = (float*)malloc(100*sizeof(float));
	float* y;
	for(int i=1;i<=100;i++)
		x[i]=i*i;
	y= fun(x,100);
	
	//Part 2

    // Opening a text file for writing
    FILE *file = fopen("binfile.bin", "wb");
    if (file == NULL) 
	{
        fprintf(stderr, "Error opening file for writing.\n");
        return 0;
    }

    // Writing mean and variance to the file
	fwrite(y, sizeof(float), 2, file);
	fclose(file);


    // Freeing the memory used for the array
	free(x);
	free(y);
	getch();
	return 0;
}
