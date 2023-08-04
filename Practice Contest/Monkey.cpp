#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;
    while (getline(cin, str))
    {
        stringstream ss(str);
        string word;
        string finalString = "";

        while (ss >> word)
        {
            finalString += word;
        }

        sort(begin(finalString), end(finalString));

        cout << finalString << endl;
    }

    return 0;
}
