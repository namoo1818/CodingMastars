def is_prime(n):
    isprime =True
    for i in range(2, int(n**(1/2)+1)):
        if (n%i) == 0:
            isprime = False
    return isprime

n = int(input())
l = []
for i in range(2, int(n**(1/2))+1):
    if (n%i) == 0:
        l.append(i)
        if (i**2) != n:
            l.append(n//i)
success = False
for i in range(len(l)//2):
    cnt = 0
    a, b = l[cnt], l[cnt+1]
    if is_prime(a)==True and is_prime(b) == True:
        print(a, b)
        success = True
        break
    cnt += 2

if success == False:
    print("IMPOSSIBLE")


