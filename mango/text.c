#include <stdio.h>
int fun(long long int a[], int n, long long i)
{
    if(i==n) return a[i-1];
    long long int r=fun(a,n,i+1);
    return r+a[i];
}
int main()
{
    int n;
    scanf("%d",&n);
    long long a[n];
    for(int i=0;i<n;i++)
    {
        scanf("%lld", &a[i]);
    }

    long long int s=fun(a, n, 0);
    printf("%lld\n", s);
    return 0;
}