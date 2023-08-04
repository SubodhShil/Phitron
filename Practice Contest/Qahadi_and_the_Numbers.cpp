#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int cnt;
        set<int> st;

        int n;
        cin >> n;

        for (int i = 1; i <= n; ++i)
        {
            int x;
            cin >> x;
            st.insert(x);
        }

        cout << n - st.size() << endl;
    }

    return 0;
}