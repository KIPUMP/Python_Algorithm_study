# backtracking은 dfs와 비슷하지만 완전히 탐색하지 않는다는 점에서 다르다

n,m = map(int,input().split())
arr = sorted(map(int,input().split()))
visited = [False] * n
result = []
def dfs() :
  if len(result) == m :
    print(*result)
    return
  else :
    remember = 0
    for i in range(n) :
      if visited[i] == False and remember != arr[i] :
        visited[i] = True
        result.append(arr[i])
        remember = arr[i]
        dfs()
        visited[i] = False
        result.pop()

dfs()

