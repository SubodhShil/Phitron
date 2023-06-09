/**
 * @file        A_Word_Capitalization.cpp
 * @author      Subodh Chandra Shil
 * @resource:   https://codeforces.com/problemset/problem/281/A
 */

#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    cin >> s;

    s[0] = toupper(s[0]);
    cout << s;

    return 0;
}