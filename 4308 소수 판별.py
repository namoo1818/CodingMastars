# 1를 빼먹지말자
import sys
n = int(input())
isprime =True
for i in range(2, int(n**(1/2)+1)):
    if (n%i) == 0:
        isprime = False
if n == 1:
    isprime = False
if isprime == True:
    print(1)
else:
    print(0)
