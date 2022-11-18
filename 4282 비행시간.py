import sys
from heapq import heappush, heappop

n = int(input())
m = int(input())
s = [[] for i in range(n + 1)]
inf = sys.maxsize
for i in range(m):
    a, b, c = map(int, input().split())
    s[a].append([b, c])

def dijkstra(start):
    dp = [inf for i in range(n + 1)]
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        w, c = heappop(heap)
        for n_n, n_w in s[c]:
            wei = n_w + w
            if dp[n_n] > wei:
                dp[n_n] = wei
                heappush(heap, [wei, n_n])
    return dp

for i in range(m):
    for j in range(m):
        v1, v2 = i, j
        v1_ = dijkstra(v1)
        cnt = v1_[v2]
        print(cnt)