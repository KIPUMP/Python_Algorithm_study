n = int(input())
a = sorted(map(int,input().split()))
b = sorted(map(int,input().split()),reverse=True)

result = 0

for i in range(n) :
  result += a[i] * b[i]

print(result)