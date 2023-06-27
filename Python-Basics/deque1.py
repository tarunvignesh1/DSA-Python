# Queue Double ended queue

from collections import deque


queue = deque()

queue.append(11)
queue.append(12)
queue.append(14)

print(queue)

queue.appendleft(16)
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)