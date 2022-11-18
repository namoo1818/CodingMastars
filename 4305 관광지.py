# 트리의 깊이를 구하는 문제

# BFS
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
            


n = int(input())
graph = [[] for _ in range(n+1)]
num = 0
for i in range(n):
    my_list = list(input())
    num = 0
    for j in my_list:
        num += 1
        if j == 'Y':
            graph[i+1].append(num)

print(graph)

visited = [False] * 9
bfs(graph, 1, visited)

