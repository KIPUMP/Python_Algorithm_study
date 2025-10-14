# https://velog.io/@yoopark/baekjoon-1197

def get_parent(x) :
    if parent[x] == x :                         # 본인 노드 밖에 없다면
        return x
    parent[x] = get_parent(parent[x])           # get_parent를 재귀방식으로 호출하면서 갱신
    return parent[x]

def union_parent(a,b) :
    a = get_parent(a)
    b = get_parent(b)
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
        
def same_parent(a,b) :
    return get_parent(a) == get_parent(b)

n,m = map(int,input().split())
parent = [i for i in range(n+1)]

answer = 0
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2]) # C(Cost)가 적은 것부터 정렬

answer = 0
for a, b, cost in edges:
    # cost가 작은 edge부터 하나씩 추가해가면서 같은 부모를 공유하지 않을 때(사이클 없을 때)만 확정
    if not same_parent(a, b):
        union_parent(a, b)
        answer += cost
print(answer)
    
