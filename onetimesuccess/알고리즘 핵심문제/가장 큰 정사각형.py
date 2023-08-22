N,M = map(int,input().split())
arr = [(list(map(int,input()))) for _ in range(N)]
result = max(arr[0])
for i in range(1,N) :
  for j in range(1,M) :
    if arr[i][j] == 1 :
      arr[i][j] = min(arr[i-1][j-1],arr[i-1][j],arr[i][j-1]) + 1
  result = max(result,max(arr[i]))

print(result ** 2)
