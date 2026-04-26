
#include <stdio.h> 
int bs(int x[], int low, int high, int key) { 
printf("1"); 
int mid; 
printf("-2"); 
while (low <= high) { 
mid = (low + high) / 2; 
printf("-3"); 
if (x[mid] == key) { 
printf("-8-9"); 
return mid; 
} 
printf("-4");  
if (x[mid] < key) { 
printf("-5"); 
low = mid + 1; 
} else { 
printf("-6");  
high = mid - 1; 
} 
printf("-7"); 
} 
printf("-8"); 
return -1; 
printf("-9"); 
} 

 
int main() { 
    int a[200], n, s, k; 
    printf("Enter the Element Length: "); 
    scanf("%d", &n); 
    printf("\nEnter the Elements Value: "); 
    for (int i = 0; i < n; i++) { 
        scanf("%d", &a[i]); 
    } 
    printf("\nEnter the Key Value: "); 
    scanf("%d", &k); 
    printf("\nPath: "); 
    s = bs(a, 0, n - 1, k); 
    if (s != -1) { 
        printf("\nThe Element %d found at index of %d\n", k, s + 1); 
    } else { 
        printf("\nThe Element %d not found.",k); 
    } 
} 