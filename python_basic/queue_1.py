from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()         # 5 삭제
queue.append(4)
queue.append(1)
queue.popleft()         # 2 삭제

print(queue)        # 처음 들어온 원소부터 출력
queue.reverse()     
print(queue)        # 나중에 들어온 원소부터 출력


