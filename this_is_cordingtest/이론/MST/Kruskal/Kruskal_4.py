import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x) :
  if parent[x] == x :
    return x
  
  parent[x] = find(parent[x])
  return parent[x]

def union(a,b) :
  if rank[a] < rank[b] :            
    parent[a] = b
  
  elif rank[a] > rank[b] :
    parent[b] = a
  
  else :
    parent[b] = a
    rank[b] += 1


v,e = map(int,input().split())        #  정점(노드) 개수 v, 간선 개수 e (정점 번호가 1..v라고 가정)
arr = []                              # 준비물 1 : 간선 목록(리스트). 각 원소는 (u, v, cost) 형태
parent = [i for i in range(v+1)]      # 준비물 2 : Union-Find용 부모 배열(처음엔 자기 자신이 대표자)
rank = [0] * (v+1)                    # 준비물 3 : 랭크(대략적 트리 높이)

for _ in range(e) :         
  a,b,c = map(int,input().split())
  arr.append((a,b,c)) 

arr = sorted(arr, key = lambda x : x[2])
mst_cost = 0
mst_edge = []

for a,b,c in arr :
  ra = find(a)
  rb = find(b)

  if ra != rb :
    union(ra,rb)
    mst_edge.append((ra,rb,c))
    mst_cost += c

print(f"최소 신장 트리 비용: {mst_cost}")
print("사용된 간선 목록:")
for u, v, cost in mst_edge:
    print(f"{u} - {v} : {cost}")

# 51928	268