#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
vector<int> adjList[N];
vector<bool> visited(N, 0);

void dfs(int s)
{
    visited[s] = 1;
    for (int child : adjList[s])
    {
        if (!visited[s])
            dfs(child);
    }
}

int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= m; ++i)
    {
        int u, v;
        cin >> u >> v;
        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }

    int s = 1;
    int requiredRoads = n - 1;
    int lastVisited = -1;   
    int needed = -1;

    for (int i = s; i <= n; ++i)
    {
        if (!visited[i])
        {
            lastVisited = i - 1;
        }
    }

    if (lastVisited == -1)
    {
        cout << 0 << endl;
        return 0;
    }

    needed = requiredRoads - (lastVisited - 1);

    for (int i = 1; i <= needed; ++i)
    {
        cout << lastVisited << " ";
        adjList[lastVisited].push_back(++lastVisited);
        cout << lastVisited << endl;
    }

    return 0;
}