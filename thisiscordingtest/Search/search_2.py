N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
cutting= []
x = arr[0]
while arr[N-1] >= x :
  total = 0
  for i in range(N) :
    if arr[i] > x :
      total += arr[i] - x

  if total == M :
    cutting.append(x)
  
  x += 1

print(max(cutting))


