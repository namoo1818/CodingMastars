# 4285 지혜로운 병원과 같은 문제

import sys
from heapq import heappush, heappop

n = int(input())
m = int(input())
s = [[] for i in range(n + 1)]
inf = sys.maxsize
for i in range(m):
    a, b, c = map(int, input().split())
    s[a].append([b, c])
    s[b].append([a, c])
v1, v2 = map(int, input().split())
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
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
cnt = min(v1_[v2], v2_[v1])
print(cnt)