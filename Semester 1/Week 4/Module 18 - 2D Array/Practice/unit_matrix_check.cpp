#include <bits/stdc++.h>
using namespace std;

class Solution1
{
public:
    void checkUnitMatrix()
    {
        int row, col;
        cin >> row >> col;

        /// edge case: unit matrix need to be a square matrix
        if (row != col)
        {
            cout << "Row and column value are not same\n";
            return;
        }

        int arr[row][col];

        /// 2D array input
        for (int i = 0; i < row; ++i)
            for (int j = 0; j < col; ++j)
                cin >> arr[i][j];

        bool isUnitMatrix = true;

        for (int i = 0; i < row; ++i)
        {
            if (arr[i][i] == 0 || arr[i][i] != 1)
                isUnitMatrix = false;
        }

        if (isUnitMatrix)
            cout << "2D array is an unit matrix\n";
        else
            cout << "2D array is not an unit matrix\n";
    }
};

int main()
{
    Solution1 sol1;
    sol1.checkUnitMatrix();

    return 0;
}