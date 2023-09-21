import sys
input = sys.stdin.readline

n = int(input())
power = list(map(int,input().split()))
power.reverse()
d = [1] * (n)

for i in range(1,n) :
  for j in range(0,i) :
    if power[j] < power[i] :
      d[i] = max(d[i],d[j]+1)

print(n-max(d))


