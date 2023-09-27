from itertools import permutations
n = int(input())
a = list(map(int,input().split()))
ans = 0
for arr in set(permutations(a,n)) :
  ans = max(ans,sum(abs(arr[i-1] - arr[i]) for i in range(1,n)))

print(ans)

