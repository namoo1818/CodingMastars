n, m = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))


def dfs():
    visited[] = True