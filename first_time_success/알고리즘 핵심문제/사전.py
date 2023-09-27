import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
d = [[0] * (m+1) for _ in range(n+1)]
for j in range(1,m+1) :
  d[0][j] = 1

for i in range(1,n+1) :
  d[i][0] = 1
  for j in range(1,m+1) :
    d[i][j] = dp[i-1][j] + d[i][j-1]

def s(n,m,k) :
  if n == 0 :
    print('z' * m) 
    return
  elif m == 0 :
    print('a' * n)
    return

  if d[n-1][m] >= k :
    print('a',end="")
    s(n-1,m,k)
  else :
    print('z',end="")
    s(n,m-1,k-d[n-1][m])

if d[n][m] < k :
  print(-1)
else :
  s(n,m,k)