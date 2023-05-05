#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int cntBeforeZero = 0;
    int arr[n];

    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < n; ++i)
    {
        if (arr[i] == 0)
            break;
        else
            cntBeforeZero++;
    }

    printf("%d\n", cntBeforeZero);

    return 0;
}