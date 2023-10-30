n,m = map(int,input().split())
arr = sorted(map(int,input().split()))
visited = [False] * n
result = []
def dfs() :
    if len(result) == m :
        print(*result)
        return 
    else :
        remember = ''
        for i in range(n) :
            if visited[i] == False and remember != arr[i] :
                visited[i] = True
                result.append(arr[i])
                remember = arr[i]
                dfs()
                result.pop()
                visited[i] = False
                

dfs()