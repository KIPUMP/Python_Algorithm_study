import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
cache = [0] * (n+1)

def f(n) :
  if cache[n] :
    return cache[n]
  
  if n == 1 :
    cache[n] = 1
  elif n == 2 :
    cache[n] = 2
  else :
    cache[n] = (f(n-1) + f(n-2)) % 10007
  return cache[n]

print(f(n))