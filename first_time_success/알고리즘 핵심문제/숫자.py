INF = 9876543210
d = [INF] * 10000001
a,b,k = map(int,input().split())

def s(n) :
  return sum(int(ch) ** k for ch in str(n))

def dfs(n) :
  if d[n] == INF :
    d[n] = 0
    d[n] = min(n,dfs(s(n)))

  else :
    if d[n] :
      return d[n]

    m = n
    nn = s(n)
    while nn != n :
      m = min(m,nn)
      nn = s(nn)
    d[n] = m
    nn = s(n)
    while nn != n :
      d[nn] = m 
      nn= s(nn)
  
  return d[n]

print(sum(dfs(i) for i in range(a,b+1)))