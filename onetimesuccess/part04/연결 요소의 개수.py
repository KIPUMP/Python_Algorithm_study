import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())
graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for _ in range(M) :
  u,v = map(int,input().split())
  graph[u][v] = True
  graph[v][u] = True

def dfs(i) :
  for j in range(1,N+1) :
    if graph[i][j] and visited[j] == False :
      visited[j] = True
      dfs(j)

for i in range(1,N+1) :
  if visited[i] == False :
    cnt += 1
    visited[i] = True
    dfs(i)

print(cnt)