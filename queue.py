from collections import deque
import sys

n = int(input())
queue = deque()


for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.append(command[1])
    if len(queue) > 0:
        if command[0] == 'front':
            print(queue[0])
        elif command[0] == 'back':
            print(queue[-1])
        elif command[0] == 'empty':
            print(0)
        elif command[0] == 'pop':
            pop = queue.popleft()
            print(pop)
        elif command[0] == 'size':
            print(len(queue))
    else:
        if command[0] == 'empty':
            print(1)
        elif command[0] == 'size':
            print(0)
        else:
            print(-1)
