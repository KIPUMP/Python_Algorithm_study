# BOJ 1197 - 최소 스패닝 트리 (Kruskal + Union-Find)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def get_parent(x):                   # 경로 압축(Path Compression)을 동반한 Find
    # x가 자신의 루트(대표자)라면 그대로 반환
    if parent[x] == x:
        return x
    # 재귀적으로 루트를 찾으며 parent[x]를 루트로 압축
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):              # 두 집합을 합침(Union)
    a = get_parent(a)
    b = get_parent(b)
    # ⚠️ 아래 로직은 단순히 '루트 번호가 작은 쪽'을 부모로 삼음.
    # 일반적으로는 rank/size를 기준으로 합치는 것이 더 효율적(union by rank/size).
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b):               # 두 원소가 같은 집합(같은 루트)에 속하는지
    return get_parent(a) == get_parent(b)

v, e = map(int, input().split())
edges = []
parent = [i for i in range(v + 1)]   # 1..v 정점을 위한 부모 배열(초기엔 자기 자신이 루트)

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))          # 무방향 간선 (a-b, 비용 c)

# 간선을 비용(가중치) 기준 오름차순으로 정렬
edges.sort(key=lambda x: x[2])

answer = 0
for a, b, c in edges:                # 비용이 낮은 간선부터 차례로 검사
    # 현재 간선을 추가해도 사이클이 생기지 않으면 채택
    if not same_parent(a, b):
        union_parent(a, b)
        answer += c                  # MST 총 비용 누적

print(answer)
