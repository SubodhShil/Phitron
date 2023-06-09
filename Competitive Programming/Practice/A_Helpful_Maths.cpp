/**
 * @file        A_Helpful_Maths.cpp
 * @author      Subodh Chandra Shil
 * @date        2023-06-09
 * @resources:  https://codeforces.com/contest/339/problem/A
 */

#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    cin >> s;
    vector<int> v;

    for (auto i : s)
    {
        if (i != '+')
            v.push_back(i - '0');
    }

    /// Dutch national flag algorithm
    int n = v.size();
    int low = 0, mid = 0, high = n - 1;

    while (mid <= high)
    {
        if (v[mid] == 1)
        {
            swap(v[low], v[mid]);
            low++;
            mid++;
        }
        else if (v[mid] == 2)
        {
            mid++;
        }
        else
        {
            swap(v[mid], v[high]);
            high--;
        }
    }

    for (int i = 0; i < v.size(); ++i)
    {
        if (i)
            cout << "+";
        cout << v[i];
    }

    return 0;
}
