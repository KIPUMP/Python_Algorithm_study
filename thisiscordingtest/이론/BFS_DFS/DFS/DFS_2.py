n,m = map(int, input().split())

graph = []

# 2차원 list 정보 입력 받기(세로길이 만큼 입력받는다)
for i in range(n) :
    graph.append(list(map(int, input())))

def dfs(x,y) :
    #범위를 벗어날 시 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >=m :
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1             #해당 노드 방문 처리(ice melt)
        # 상하좌우 위치 재귀적 호출
        dfs(x-1,y)              #좌
        dfs(x,y-1)              #하
        dfs(x+1,y)              #우
        dfs(x,y+1)              #상
        return True
    return False

result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i,j) == True:
            result +=1

print(result)
