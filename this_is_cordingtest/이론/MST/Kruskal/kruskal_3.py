# https://www.acmicpc.net/problem/1197
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(parent,x) :
  if parent[x] == x :
    return x 
  
  parent[x] = find(parent,parent[x])
  return parent[x]

def union(parent,rank,a,b) :
  if rank[a] < rank[b] :        
    parent[a] = b
  
  elif rank[a] > rank[b] :
    parent[b] = a
  
  else :
    parent[b] = a
    rank[a] += 1


v,e = map(int,input().split())
arr = []
parent = [i for i in range(v+1)]
rank = [0] * (v+1)

for _ in range(e) :
  a,b,c = map(int,input().split())
  arr.append((a,b,c))

arr = sorted(arr, key = lambda x : x[2])
answer = 0

for a,b,c in arr :
  ra = find(parent,a)
  rb = find(parent,b)

  if ra != rb :
    union(parent,rank,ra,rb)
    answer += c

print(answer)
