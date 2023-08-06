#include <bits/stdc++.h>
using namespace std;

#define superfast ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define ll long long
#define yes {cout<<"YES"<<endl;}
#define no {cout<<"NO"<<endl;}

/// for loops
#define fori(x) for( int i = 0; i < x; i++)
#define forj(x) for( int j = 0; j < x; j++)

void ans()
{
    string str = "codeforces", str2;
    cin >> str2;
    int unmatchedCnt = 0;
    int i = 0, j = 0;

    while(i < 10 && j < 10)
    {
        if(str[i] != str2[j])
        {
            ++unmatchedCnt;
        }
        ++i, ++j;
    }

    cout << unmatchedCnt << endl;
}

int main()
{
    superfast
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i)
    {
        // cout << "Case " << i << ": ";
        ans();
    }

    return 0;
}