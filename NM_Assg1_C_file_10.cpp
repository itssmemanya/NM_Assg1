#include <stdio.h>

int main() 
{
    // Opening the binary file for reading
    FILE *file = fopen("binfile.bin", "rb");
    if (file == NULL) {
        fprintf(stderr, "Error opening file for reading.\n");
        return 0;
    }

    // Reading the result from the binary file
    float y[2];
    fread(y, sizeof(float), 2, file);
    fclose(file);

    // Printing the result
    printf("Mean : %.2f \n", y[0]);
    printf("Variance : %.2f \n", y[1]);

    return 0;
}

