from functools import reduce
n = 100
# 람다식 구현
print(reduce((lambda r, x : r-set(range(x**2,n,x)) if (x in r) else r),
range(2,int(n**0.5)),set(range(2,n))))
# 반복문으로 구현
a = [False,False] + [True] * (n-1)
primes = []

for i in range(2,n+1) :
  if a[i] :
    primes.append(i)
    for j in range(2*i,n+1,i) :
      a[j] = False
print(primes)