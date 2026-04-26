#include <stdio.h> 
#include <stdlib.h> 
int main() { 
int a[10][10], b[10][10], result[10][10]; 
int p, q, r, s, i, j, k; 
printf("Enter rows and columns of A Matrix: "); 
scanf("%d %d", &p, &q); 
printf("Enter rows and columns of B Matrix: "); 
scanf("%d %d", &r, &s); 
if (q != r) { 
printf("Test Case 2: Matrix Multiplication is not possible\n"); 
printf("The columns of A Matrix are not equal to rows of B Matrix\n"); 
printf("Case 2: Failure\n"); 
return 0; 
} 
printf("Test Case 1: Matrix Multiplication can be done\n"); 
printf("Case 1: Success\n"); 
printf("Enter the elements of Matrix A:\n"); 
for (i = 0; i < p; i++) { 
for (j = 0; j < q; j++) { 
if (scanf("%d", &a[i][j]) != 1) { 
printf("Test Case 3: Matrix Multiplication is not possible\n"); 
printf("One or more values are not an integer\n"); 
printf("Case 3: Failure\n"); 
return 0; 
} 
} 
 
    } 
    printf("Enter the elements of Matrix B:\n"); 
    for (i = 0; i < r; i++) { 
        for (j = 0; j < s; j++) { 
            if (scanf("%d", &b[i][j]) != 1) { 
                printf("Test Case 3: Matrix Multiplication is not possible\n"); 
                printf("One or more values are not an integer\n"); 
                printf("Case 3: Failure\n"); 
                return 0; 
            } 
        } 
    } 
    for (i = 0; i < p; i++) { 
        for (j = 0; j < s; j++) { 
            result[i][j] = 0; 
            for (k = 0; k < q; k++) { 
                result[i][j] += a[i][k] * b[k][j]; 
            } 
        } 
    } 
    printf("The result of matrix multiplication is:\n"); 
    for (i = 0; i < p; i++) { 
        for (j = 0; j < s; j++) { 
            printf("%d\t", result[i][j]); 
        } 
        printf("\n"); 
    } 
    return 0; 
} 