d = [0] * 100
N = int(input())
arr = list(map(int,input().split()))

d[0] = arr[0]
d[1] - max(arr[0],arr[1])

for i in range(2,N) :
  d[i] = max(d[i - 1],arr[i-2] + arr[i])

print(d[N-1])