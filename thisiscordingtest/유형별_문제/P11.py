import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
dummy = [[0] * (N+1) for _ in range(N+1)]
info = []
for _ in range(K) :
  a,b = map(int,input().split())
  dummy[a][b] = 1

L  = int(input())

for _ in range(L) :
  X,C = input().split()
  info.append((int(x),c))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction,c) :
  if c == "L" :
    direction = (direction - 1) % 4
  else :
    direction = (direction + 1) % 4
  return direction

def simulate() :
  x,y = 1,1
  dummy[x][y] = 2
  direction = 0
  time = 0
  index = 0 
  q = [(x,y)]
  while True :
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and dummy[nx][ny] != 2:
      if dummy[nx][ny] == 0 :
        dummy[nx][ny] = 2
        q.append((nx,ny))
        px,py = q.pop(0)
        dummy[px][py] = 0

      if dummy[nx][ny] == 1 :
        dummy[nx][ny] = 2
        q.append((nx,ny))

    else :
      time += 1
      break
    x,y = nx,ny
    time += 1
    if index < l and time == info[index][0] :
      direction = tuen(direction,info[index][1])
      index += 1
  return time

print(simulate())

