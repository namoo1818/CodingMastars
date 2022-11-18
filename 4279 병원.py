# -*- coding: utf-8 -*-
import sys
n = int(input())
array = list(map(int, input().split()))
cnt = 0
for i in range(1, n):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        isit = False
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
            isit = True
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
        if isit == True:
            cnt += 1
print(cnt)