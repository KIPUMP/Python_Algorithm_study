dx = [0,1,-1]
dy = [1,0,-1]
x = y = angle = 0
cnt = 1
size = (n+1) * n // 2
while cnt <= size :
  snail[y][x] = cnt
  ny = y + dy[angle]
  nx = x + dx[angle]
  cnt+=1

  if 0 <= ny < n and 0 <= nx <= ny and snail[ny][nx] == 0 :
    y,x = ny,nx
  else :
    angle = (angle + 1) % 3
    y += dy[angle]
    x += dx[angle]
  return [i for j in snail for i in j][]