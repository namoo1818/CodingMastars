# bfs문제

n, m = map(int, input().split())
dalgona = []
yamyam = [[0]*m for _ in range(n)] # 들린 위치를 저장하기 위한 리스트
steps = [(-1,0),(1,0),(0,-1),(0,1)]
count = 0 # 달고나 개수
for i in range(n):
    dalgona.append(list(map(int, str(input()))))
for i in range(n):
    for j in range(m):
        if dalgona[i][j] == 0:
            new_dal = True
            yamyam[i][j] += 1
            for step in steps:
                k = i + step[0]
                l = j + step[1]
                if k>=0 and k<n and l>=0 and l<m :
                    if yamyam[k][l] == 1:
                        new_dal = False
            if new_dal == True:
                count += 1
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