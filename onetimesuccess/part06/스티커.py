import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
  n = int(input())
  sticker = []
  for _ in range(2) :
    sticker.append(list(map(int,input().split())))
  d = [[0] * n for _ in range(2)]
  for i in range(2) :
    d[i][0] = sticker[i][0]
    if n > 1 :
      d[i][1] = sticker[i ^ 1][0] + sticker[i][1]
    
  for j in range(2,n) :
    for i in range(2) :
      d[i][j] = max(d[i ^ 1][j-2],d[i^1][j-1]) + sticker[i][j]
  
  print(max(d[0][n-1],d[1][n-1]))

