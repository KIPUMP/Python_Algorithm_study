from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(4)
queue.append(1)
queue.popleft()

print(queue)
queue.reverse()     #역행출력
print(queue)


