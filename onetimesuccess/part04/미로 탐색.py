from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dy = (0,1,0,-1) 
dx = (1,0,-1,0) 

board = [input() for _ in range(N)]
chk = [[False] * M for _ in range(N)]
queue = deque()
queue.append((0,0,1))
chk[0][0] = True

def is_valid_coord(y,x):
  return 0 <= y < N and 0 <= x < M

while queue :
  y,x,d = queue.popleft()

  if y == N - 1 and x == M - 1 :
    print(d)
    break
  
  for k in range(4) :
    ny = y + dy[k]
    nx = x + dx[k]
    nd = d + 1
    
    if is_valid_coord(ny,nx) and board[ny][nx] == '1' and chk[ny][nx] == False :
      chk[ny][nx] = True
      queue.append((ny,nx,nd))



