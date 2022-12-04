# 우선순위 큐 사용 다익스트라 알고리즘
import heapq
import sys
input = sys.stdin.readline  
INF = int(1e9)              # 무한

#  노드의 개수와 간선의 개수를 입력
n,m = map(int,input().split())
#  시작 노드와 번호를 입력
start = int(input())
# 노드 정보 리스트
graph = [[] for i in range(n+1)]
# 방문 노드 리스트
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m) :
    a,b,c = map(int, input().split())
    # a 번 노드에서 b 번 노드로 가는 비용이  c
    graph[a].append((b,c))
    
def dijkstra(start) :
    q = []
    # 시작노드로 가기위한 최단거리 0으로 설정, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:                #큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        #  현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
# 다익스트라 알고리즘 수행
dijkstra(start)
# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1) :
    if distance[i] == INF :
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else :
        print(distance[i])
            
        