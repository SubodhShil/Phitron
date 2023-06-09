#include <bits/stdc++.h>
using namespace std;

int main()
{
    int k, n, w;
    cin >> k >> n >> w;

    int totalPrice = k * (w * (w + 1) / 2);
    (totalPrice - n > 0) ? cout << totalPrice - n : cout << 0;

    return 0;
}