n = int(input())
t = []
p = []
d = [0] * (n+1)
for _ in range(n) :
  x,y = map(int,input().split())
  t.append(x)
  p.append(y)

max_val = 0

for i in range(n-1,-1,-1) :
  time = t[i] + i 
  if time <= n :
    d[i] = max(p[i] + d[time],max_value)
    max_val = d[i]
  else :
    d[i] = max_val

print(max_val)