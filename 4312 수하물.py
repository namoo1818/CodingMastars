# 백준 1202번 보석 도둑과 같은 문제
import sys
import heapq

n, k = map(int, input().split())
goods = []
for _ in range(n):
    heapq.heappush(goods, list(map(int, input().split())))
bags = []
for _ in range(k):
    bags.append(int(input()))
bags.sort()

cost = 0
tmp_goods = []
for bag in bags:
    while goods and bag >= goods[0][0]:
        heapq.heappush(tmp_goods, -heapq.heappop(goods)[1])
    if tmp_goods:
        cost -= heapq.heappop(tmp_goods)
    elif not goods:
        break
print(cost)
