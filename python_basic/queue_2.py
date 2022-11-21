from collections import deque

queue = deque()

queue.append(3)
queue.append(5)
queue.append(4)
queue.pop()                         #입구에서 제거

queue.append(1)
queue.append(7)
queue.popleft()                     #출구에서 제거

queue.reverse()
print(queue)