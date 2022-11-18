# 달고나 문제임
import sys
sys.setrecursionlimit(100000)
from collections import deque

m, n, k = map(int, input().split())
graph = [[1]*m for _ in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 0

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
print(count)

