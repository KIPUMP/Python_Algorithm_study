from collections import deque

queue = deque()

def bfs(graph,start,visited) :
  queue.append(start)                     # queue에 노드 삽입
  visited[start] = True
  while queue :                     
    v = queue.popleft()                   # queue가 있는 동안 queue의 원소를 하나씩 뽑는다
    print(v,end=" ")
    for i in graph[v] :
      if not visited[i] :
        queue.append(i)
        visited[i] = True

graph = [
    [],										# 0 번 노드는 null
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]  

visited = [False] * 9 

bfs(graph,1,visited)