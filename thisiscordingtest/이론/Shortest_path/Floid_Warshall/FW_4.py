INF = int(1e9)
n,m = map(int,input().split())
arr = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1) :
  for j in range(1,n+1) :
    if i == j :
      arr[i][j] = 0

for i in range(m) :
  a,b,c = map(int,input().split())
  arr[a][b] = c

for k in range(1,n+1) :
  for a in range(1,n+1) :
    for b in range(1,n+1) :
      arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])


for i in range(1,n+1) :
  for j in range(1,n+1) :
    if arr[i][j] == INF :
      print("INFINITY",end=" ")
    else :
      print(arr[i][j],end=" ")
  print()


# 4 7
# 1 2 4
# 1 4 6
# 2 1 5
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2