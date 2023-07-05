def GCD(a,b) :
  if b == 0 :
    return a 
  else :
    return GCD(b,a%b)

def LCM(x,y) :
  return (x * y) // GCD(x,y)

n,m = map(int,input().split())

print(GCD(n,m))
print(LCM(n,m))