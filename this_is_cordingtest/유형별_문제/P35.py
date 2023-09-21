import sys
input = sys.stdin.readline
n = int(input())
d = [1] * (1003)
for i in range(1,n+1) :
    d[i] = min(d[i-1]*2, d[i-1]*3,d[i-1]*5) 
    print(d[i])


d.sort()
print(d[n])






