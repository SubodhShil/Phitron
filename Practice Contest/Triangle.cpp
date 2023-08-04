#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;
    if ((a + b + c) % 3 == 0 && (a > 0 && b > 0 && c > 0))
        cout << "Yes\n";
    else
        cout << "No\n";

    return 0;
}