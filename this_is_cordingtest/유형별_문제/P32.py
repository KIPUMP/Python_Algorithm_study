import sys
input = sys.stdin.readline

n = int(input())
d = [[0] * (n+1) for _ in range(n+1)]
for i in range(n) :
  num = list(map(int,input().split()))
  for j in range(len(num)) :
    d[i][j] = num[j]

result = d[0][0]
for i in range(1,n+1) :
  for j in range(i+1) :
    d[i][j] = max(d[i-1][j] + d[i][j] , d[i-1][j-1] + d[i][j])

print(max(d[n]))
  
  

