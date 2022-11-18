# 시간초과

import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

l = []
answer = 0
for case in permutations(A):
    mid_sum = 0
    answer = 0
    for i in range(N):
        mid_sum = abs(case[-i] - case[-N+1])
        answer = max(mid_sum, answer)
    l.append(answer)

print(min(l))