import sys
input = sys.stdin.readline

n,m,start = map(int,input().split())

visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)



