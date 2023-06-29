def GCD(m,n) :
  if n == 0 :
    return m 
  else :
    return GCD(n,m%n)

def LCM(m,n) :
  return (m*n) // GCD(m,n)


m,n = map(int,input().split())

print(GCD(m,n))
print(LCM(m,n))