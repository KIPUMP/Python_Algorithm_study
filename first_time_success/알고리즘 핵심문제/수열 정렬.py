n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
chk = [False] * n 
p = []
for i in a :
  for j in range(b.index(i),n) :
    if i == b[j]and chk[j] :
      chk[j] = True
      p.append(j)
      break

print(" ".join(map(str,p)))