#include <stdio.h>

void swap(int *x,int *y);
void quicksort(int list[],int m,int n);

int main()
{
    int list[] = {39,82,38,73,19,75,29,70,3,92};
    int size = (int) (sizeof(list)/sizeof(int));

    quicksort(list,0,size-1);

    for(int i=0; i<10; i++)
        printf("%d\t",list[i]);

	return 0;
}

void swap(int *x,int *y)
{
    int tmp;
    tmp = *x;
    *x = *y;
    *y = tmp;
}


void quicksort(int list[],int m,int n)
{
    int key,i,j,k;
    if( m < n)
    {
        k = (m+n)/2;
        swap(&list[m],&list[k]);
        key = list[m];
        i = m+1;
        j = n;
        while(i <= j)
        {
            while((i <= n) && (list[i] <= key))
                i++;
            while((j >= m) && (list[j] > key))
                j--;
            if( i < j)
                swap(&list[i],&list[j]);
        }
        /* swap two elements */
        swap(&list[m],&list[j]);

        /* recursively sort the lesser list */
        quicksort(list,m,j-1);
        quicksort(list,j+1,n);
    }
}
