import sys

n,k = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
s,x,y = map(int,input().split())

dx = [0, 1, 0 ,-1]
dy = [1 ,0 ,-1 ,0]

def virus(x,y,k):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 0:
            data[nx][ny] = k

            
v = 1
for _ in range(s):
    for i in range(n):
        for j in range(n):
            if v > k :
                v = 1
            if data[i][j] == v:
                virus(i,j,v)
                v += 1
                

print(data)
print(data[x-1][y-1])
