n,m = map(int,input().split())
min_val = []
for _ in range(n) :
  arr = list(map(int,input().split()))
  min_val.append(min(arr))


print(max(min_val))
  