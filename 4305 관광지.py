# 다익스트라 문제
import heapq
import sys
# input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
num = 0
for i in range(n):
    my_list = list(input())
    num = 0
    for j in my_list:
        num += 1
        if j == 'Y':
            graph[i+1].append((num, 1))



def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dis = 0
for i in range(n):
    start = i+1
    print(dijkstra(start))
    for j in range(1, n+1):
        if distance[j] != INF and distance[j] > dis:
            dis = distance[j]
print(dis)