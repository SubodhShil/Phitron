#include <bits/stdc++.h>
using namespace std;

class Solution1
{
public:
    bool isNullMatrix(int *arr)
    {
    }
};

int main()
{
    int row, col;
    cin >> row, col;
    int arr[row][col];

    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < col; ++j)
            cin >> arr[i][j];
    }

    return 0;
}