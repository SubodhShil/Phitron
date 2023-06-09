#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        for (int i = 1; i <= n; ++i)
        {
            if (i == 1 or i == n)
                cout << 1;
            else
                cout << 0;
        }

        cout << endl;
    }

    return 0;
}