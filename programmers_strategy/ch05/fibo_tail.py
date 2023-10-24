def fib_tail(n,first,second) :
  if n <= 1 :
    return second
  return fib_tail(n-1,second,first+second)


print(fib_tail(35,0,1))