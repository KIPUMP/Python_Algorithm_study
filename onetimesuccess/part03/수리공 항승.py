coord = [False] * 1001
N,L = map(int,input().split())
for i in map(int,input().split()) :
  coord[i] = True

result = 0
x = 0

while x <= 1000 :
  if coord[x] :
    result += 1
    x += L
  else :
    x += 1

print(result)