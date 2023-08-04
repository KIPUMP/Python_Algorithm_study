import sys
sys.setrecursionlimit(10**6)
N,M,K = map(int,input().split())
board = [['.'] * (M) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dy = (0,1,0,-1) 
dx = (1,0,-1,0)

for _ in range(K) :
  r,c = map(int,input().split())
  board[r-1][c-1] = '#'

def is_valid_coord(y,x) :
  return 0 <= y < N and 0 <= x < M

sz = 0
ans = 0
def dfs(y,x) :
  global ans,sz

  visited[y][x] = True
  sz += 1
  ans = max(ans,sz)

  for k in range(4) :
    ny = y + dy[k]
    nx = x + dx[k]
    if is_valid_coord(ny,nx) and visited[ny][nx] == False and board[ny][nx] == '#' :
      dfs(ny,nx)

for i in range(N) :
  for j in range(M) :
    if visited[i][j] == False and board[i][j] == '#' :
      sz = 0
      dfs(i,j)

print(ans)