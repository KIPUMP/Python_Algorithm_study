from collections import deque

N,M = map(int,input().split())
gr = [[False] * N for _ in range(N)]
for _ in range(M) :
  a,b = map(int,input().split())
  gr[a-1][b-1] = gr[b-1][a-1] = True

# result = -1
# result_total = 987654321
dist = [[0] * N for _ in range(N)] 

def bfs(start,goal) :
  chk = [False] * N 
  dq = deque()
  chk[start] = True
  dq.append((start,0))
  while dq :
    now,d = dq.popleft() 
    if now == goal :
      return d
    for nxt in range(N) :
      if gr[now][nxt] and not chk[nxt] :
        chk[nxt] = True
        dq.append((nxt,d+1))

result = []
for i in range(N) : 
  total = 0
  for j in range(N) :
    if i != j :
      if dist[i][j] == 0 :
        dist[i][j] = dist[j][i] = bfs(i,j)

      total += dist[i][j]
  
  result.append(total)

  # if result_total > total :
  #   result = i
  #   result_total = total

# print(result + 1)
print(result.index(min(result))+1)