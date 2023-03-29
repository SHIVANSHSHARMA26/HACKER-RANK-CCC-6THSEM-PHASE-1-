#include <bits/stdc++.h>
using namespace std;

int n, m, xs, ys, xe, ye;
int a[1005][1005];
bool vis[1005][1005];

void DFS(int x, int y) {
    if (x == xe && y == ye) {
        cout << "Hie Barua\n";
        exit(0);
    }
    vis[x][y] = true;
    if (x > 1 && !vis[x - 1][y] && a[x - 1][y] <= a[x][y]) DFS(x - 1, y);
    if (x < n && !vis[x + 1][y] && a[x + 1][y] <= a[x][y]) DFS(x + 1, y);
    if (y > 1 && !vis[x][y - 1] && a[x][y - 1] <= a[x][y]) DFS(x, y - 1);
    if (y < m && !vis[x][y + 1] && a[x][y + 1] <= a[x][y]) DFS(x, y + 1);
}

int main() {
    cin >> n >> m >> xs >> ys >> xe >> ye;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            cin >> a[i][j];
    DFS(xs, ys);
    cout << "No Chance\n";
    return 0;
}
