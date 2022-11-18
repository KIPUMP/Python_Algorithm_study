from collections import deque

queue = deque()

queue.append(3)
queue.append(5)
queue.append(4)
queue.pop()

queue.append(1)
queue.append(7)
queue.popleft()

queue.reverse()
print(queue)