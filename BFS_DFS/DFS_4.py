#dfs는 stack 구조를 활용한다, 오른쪽 부터 깊이 우선 탐색
def DFS(graph, start_node):
    #visted 리스트와 need_visited 리스트 생성
    visited = list()
    need_visited = list()
    #출발 node need_visited 리스트에 삽입
    need_visited.append(start_node)
    #need_visited node가 없을 때 까지 반복
    while need_visited :
        node = need_visited.pop()
        if node not in visited :
            visited.append(node)
            need_visited.extend(graph[node])
    print(visited)


graph = dict()

graph['A'] = ['B','C']
graph['B'] = ['A','D']
graph['C'] = ['A','G','H','I']
graph['D'] = ['B','E','F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C','J']
graph['J'] = ['I']

DFS(graph, 'A')