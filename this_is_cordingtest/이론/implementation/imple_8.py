n = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
motion = list(input().split())
x,y = 1,1
for i in motion :
  if i == 'L' :
    nx,ny = x+dx[0],y+dy[0]
  if i == 'R' :
    nx,ny = x+dx[1],y+dy[1]
  if i == 'U' :
    nx,ny = x+dx[2],y+dy[2]
  if i == 'D' :
    nx,ny = x+dx[3],y+dy[3]
  if nx < 1 or ny < 1 or nx > n or ny > n :
    continue
  x,y = nx,ny

print(x,y)
