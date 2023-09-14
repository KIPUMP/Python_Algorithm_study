import sys
from collections import deque
input = sys.stdin.readline

N,M,K,X = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M) :
    a,b = map(int,input().split())
    graph[a].append(b)
    
distance = [-1] * (N+1)
distance[X] = 0

def bfs(graph,start,distance) :
    queue = deque([start])
    distance[start] = 0
    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if distance[i] == -1 :
                distance[i] = distance[v] + 1
                queue.append(i)
                
check = False 
bfs(graph,X,distance)
for i in range(1,N + 1) :
    if distance[i] == K :
        print(i)
        check = True

if check == False :
    print(-1)
        
