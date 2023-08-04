#include <bits/stdc++.h>
using namespace std;

void ans()
{
    string str;
    cin >> str;

    bool zazaTurn = 1;
    int cnt = 0;

    for (int i = 0; i < str.size(); ++i)
    {
        if (str[i] == '1' && zazaTurn)
        {
            ++cnt;
        }
        else if (str[i] == '0' && zazaTurn)
        {
            zazaTurn = 0;
        }
        else if (str[i] == '0' && !zazaTurn)
            zazaTurn = 1;
    }

    cout << cnt << endl;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        ans();
    }

    return 0;
}