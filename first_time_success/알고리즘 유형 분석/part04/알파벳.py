from collections import deque
R,C = map(int,input().split())
dy = (0,1,0,-1)
dx = (1,0,-1,0)

board = [input() for _ in range(R)]
chk = [[set() for _ in range(C)] for _ in range(R)]
def is_vaild_coord(y,x) :
  return 0 <= y < R and 0 <= x < C
result = 0

queue = deque()
chk[0][0].add(board[0][0])
queue.append((0,0,board[0][0]))
while queue :
  y,x,s = queue.popleft()
  result = max(result,len(s))
  for k in range(4) :
    ny = y + dy[k]
    nx = x + dx[k]
    if is_vaild_coord(ny,nx) and board[ny][nx] not in s :
      ns = s + board[ny][nx]
      if ns not in chk[ny][nx] :
        chk[ny][nx].add(ns)
        queue.append((ny,nx,ns))

print(result)
