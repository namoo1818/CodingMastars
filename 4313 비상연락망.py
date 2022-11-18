# 트리의 높이를 구하는 문제
# BFS
# import sys

# from collections import deque

# def bfs(node):
#     queue = deque()
#     queue.append(node)
#     while queue:
#         node = queue.popleft()
#         for n in graph[node]:
#             if check[n] == 0:
#                 check[n] = check[node]+1
#                 queue.append(n)
            
# n = int(input())
# l = list(map(int, input().split()))
# graph = [[] for _ in range(n+1)]
# num = 0
# for i in l:
#     num += 1
#     graph[num].append(i)
#     graph[i].append(num)
# check = [0]*(n+1)
# bfs(1)
# print(check[n]-1 if check[n] > 0 else -1)

n = int(input())
l = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
num = 0
for i in l:
    num += 1
    graph[num].append(i)
visited = [False] * (n+1)
result = []

print(graph)

def dfs(v, num):
  num += 1
  visited[v] = True

  if v == n:
    result.append(num)

  for i in graph[v]:
    if not visited[i]:
      dfs(i, num)

dfs(1, 0)
if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)









"""
제 5 특공대에서는 위급시 상황 전달을 빠르게 진행하기 위해 비상연락망을 만들었습니다. 비상연락망은 1번부터 N번까지 차례로 번호매겨진 부대 각 부서의 상급부서가 적혀있습니다. 대대장이 속한 최고상급부서는 1번입니다. 



대대장은 비상연락망을 이용하여 상급부서에서 예하부서로 상황을 전달하는 방식으로 훈련을 진행하려고 합니다. 직속상관에게 상황을 전달받아 바로 밑의 부서에 상황을 전해주는 시간은 단 1초로 규정할 때, 훈련을 시작하고 모든 부서가 상황을 전달받는 데에 걸리는 시간을 출력하는 프로그램을 작성해주세요.


예제 입력1

10
1 1 1 1 1 1 1 1 1 1

예제 출력1

1

예제 입력2

10
1 1 2 2 4 4 4 7 5 5

예제 출력2

4

입력값 설명

첫째 줄에 부서의 수 N이 주어집니다. (1 ≤ N ≤ 500)
둘째 줄에 각 부서의 상위부서의 번호 M(1 ≤ M ≤ 500)이 공백으로 구분되어 주어집니다.
대대장이 속한 1번부서의 상위번호는 항상 1로 주어집니다.

출력값 설명

첫째 줄에 모든 부서가 상황을 전달받는데 걸리는 시간을 출력하세요
"""