def BFS(graph, start_node):
    # graph에서 BFS 된 list와 BFS 되야 할 list생성 
    visited = list()
    need_visited = list()

    #시작 노드 visited 리스트에 넣기
    need_visited.append(start_node)
    # need_ visited 리스트가 없을 때까지 반복 수행
    while need_visited:
        node = need_visited.pop(0)

        # visited에 node가 없을 때
        if node not in visited:
            #visited 리스트에 node  넣고,
            visited.append(node)
            # 해당 node에 연결된 노드 extand 사용해서  need_visited 리스트에 넣기
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

BFS(graph, 'A')