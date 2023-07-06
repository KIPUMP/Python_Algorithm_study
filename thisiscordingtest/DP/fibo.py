d = [0] * 100

def fibo(x) :
  if x == 1 or x == 2 :
    return 1
  
  if d[x] != 0 :
    return d[x]
  
  d[x] = fibo(x-2) + fibo(x-1)
  return d[x]


print(fibo(99))