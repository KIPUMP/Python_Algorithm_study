def factorial(n) :
  result = 1
  for i in range(1,n+1) :
    result *= i
  return result


def factorial_recursive(n) :
  if n <= 1 :
    return 1

  else :
    return n * factorial_recursive(n-1)

print('반복적 구현 : ',factorial(10))
print('재귀적 구현 : ',factorial_recursive(10))
