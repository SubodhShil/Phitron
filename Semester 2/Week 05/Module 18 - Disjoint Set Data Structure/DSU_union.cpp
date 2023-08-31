#include <bits/stdc++.h>
using namespace std;

vector<int> parent(1000, -1);

/// Time complexity: O(N)
int find(int node)
{
    while (parent[node] != -1)
    {
        node = parent[node];
    }

    return node;
}

void dsu_union(int a, int b)
{
    int leaderA = find(a);
    int leaderB = find(b);

    if (leaderA != leaderB)
    {
        // parent[leaderB] = leaderA;
        /// or vice versa
        parent[leaderA] = leaderB;
    }
}

int main()
{
    int n, e;
    cin >> n >> e;
    while (e--)
    {
        int u, v;
        cin >> u >> v;
        dsu_union(u, v);
    }

    return 0;
}