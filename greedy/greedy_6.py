n,m,k = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
first_val = num[n-1]
second_val = num[n-2]
total = 0
while m > 0 :
  for _ in range(k) :
    total += first_val
    m -= 1
  
  total += second_val
  m-=1

print(total)

  



