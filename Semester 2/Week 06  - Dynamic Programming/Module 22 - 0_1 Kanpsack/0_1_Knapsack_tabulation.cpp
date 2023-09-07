#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, capacity;
    cin >> n >> capacity;
    int dp[n + 1][capacity + 1];
    int values[n], weight[n];

    for (int i = 0; i <= n * 2; ++i)
    {
        if (i <= n)
            cin >> values[i];
        else
            cin >> weight[i];
    }

    for (int i = 0; i <= n; ++i)
    {
        for (int j = 0; j <= capacity; ++j)
        {
            /// matches to recursion base case
            if (i == 0 || j == 0)
                dp[i][j] = 0;

            if ()
        }
    }

    return 0;
}