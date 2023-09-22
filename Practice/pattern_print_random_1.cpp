#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    char arr[n + 1][n + 1];
    memset(arr, ' ', sizeof(arr));

    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= n; ++j)
        {
            if (i == 1)
                arr[i][j] = j + '0';
            if (j == 1)
                arr[i][1] = i + '0';
            if (j == n)
                arr[i][n] = n + '0';
            if (i == n)
                arr[n][j] = n + '0';
        }
    }

    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= n; ++j)
        {
            cout << arr[i][j];
        }
        cout << endl;
    }

    return 0;
}

/*

Input:
4
Output:
1234
2  4
3  4
4444

 */