#include <bits/stdc++.h>
using namespace std;

int knapsack(int n, int limit, int v[], int w[], int res = 0)
{
    if(n == 0) 
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, limit;
        cin >> n >> limit;

        int values[n], weight[n];
        for (int i = 0; i < n * 2; ++i)
        {
            if (i < n)
                weight[i];
            else
                values[i];
        }

        int ans = 0;
        cout << knapsack(n, limit, values, weight, ans) << endl;
    }

    return 0;
}