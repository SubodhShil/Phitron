/**
 * @file        Encoding_Message.cpp
 * @author      Subodh Chandra Shil
 * @date        2023-06-11
 * @resources:  https://www.codechef.com/problems/ENCMSG
 */

#include <bits/stdc++.h>
using namespace std;

int encodingFormula(char ch)
{
    return 122 + 97 - (2 * int(ch));
}

int main()
{
    /// formula: 122 - (character_value_in_ASCII - 97) - character_value_in_ASCII
    /// = 122 + 97 - (2 * character_value_in_ASCII)

    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        string s;
        cin >> s;

        if (n & 1)
        {
            s[n - 1] = s[n - 1] + encodingFormula(s[n - 1]);
            n = n - 1;
        }

        for (int i = 0; i < n; i += 2)
        {
            swap(s[i], s[i + 1]);
            s[i] = s[i] + encodingFormula(s[i]);
            s[i + 1] = s[i + 1] + encodingFormula(s[i + 1]);
        }

        cout << s << endl;
    }

    return 0;
}