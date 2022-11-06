"""
첫시도(틀림)
달고나가 다음과 같은 모양일 때 달고나를 2개로 인식한다
010
000 
이는 yamyam 리스크에 들린 위치를 순서대로 저장하면서 생긴 오류다
다음 행에서 달고나가 이어지는 경우를 예상하지 못했다

n, m = map(int, input().split())
dalgona = []
yamyam = [[0]*m for _ in range(n)] # 들린 위치를 저장하기 위한 리스트
steps = [(-1,0),(1,0),(0,-1),(0,1)]
count = 0 # 달고나 개수
for i in range(n):
    dalgona.append(list(map(int, input())))
for i in range(n):
    for j in range(m):
        if dalgona[i][j] == 0:
            new_dal = True
            yamyam[i][j] = 1
            for step in steps:
                k = i + step[0]
                l = j + step[1]
                if k>=0 and k<n and l>=0 and l<m and yamyam[k][l] == 1:
                    new_dal = False   
        else:
            new_dal = False

        if new_dal == True:
            count += 1
print(count)

"""
# DFS 풀이

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == '0':
        graph[x][y] = '1'
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
print(count)



# BFS 풀이

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

def bfs(x, y):
    queue = deque(())
    queue.append((x, y))

    if graph[x][y] == 1:
        return 0

    while queue:
        x, y = queue.popleft()
        graph[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
    return 1


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        count += bfs(i, j)

print(count)


"""
신입사원 종구는 달고나를 너무 좋아해서 매일 엄청난 양의 달고나를 먹습니다. 결국 종구는 참지 못하고 직접 달고나를 해먹고자 달고나 판을 구매했습니다. 종구가 구매한 달고나 판은 다양한 크기의 구멍이 여러개 있습니다.



달고나를 만들 때는 판 전체에 설탕물을 부어야 하고, 달고나 판의 특성상 두 구멍이 상하좌우로 붙어있으면 하나의 달고나로 합쳐집니다. 달고나 판의 구멍들의 위치가 주어지면, 달고나를 한 번 만들 때 몇 개의 달고나가 만들어지는지 출력하는 프로그램을 작성해주세요.


예제 입력1

2 3
010
101

예제 출력1

3

예제 입력2

5 5
00100
00100
11111
00100
00100

예제 출력2

4

입력값 설명

첫 번째 줄에 달고나 판의 세로 길이 N과 가로 길이 M이 주어집니다. (1 ≤ N, M ≤ 100)
두 번째 줄부터 N+1번째 줄까지 0과 1로 달고나 판의 형태가 주어집니다. 구멍이 뚫린 곳은 0, 막혀있는 곳은 1입니다.

출력값 설명

달고나를 한 번 만들 때 몇 개의 달고나가 만들어지는지 출력합니다.
"""