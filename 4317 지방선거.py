# 더 짧게 줄이는 방법이 있다
my_input = []
n = int(input())
for i in range(n):
    my_input.append(int(input()))
max_input = max(my_input)
my_list = [0] * max_input
for i in my_input:
    my_list[i-1] +=1
print(my_list.index(max(my_list))+1)

