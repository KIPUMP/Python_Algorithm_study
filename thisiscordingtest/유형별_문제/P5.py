from itertools import combinations

N,M = map(int,input().split())
K = list(map(int,input().split()))
cnt = 0
for i in combinations(K,2) :
  if i[0] != i[1] :
    cnt += 1

print(cnt)