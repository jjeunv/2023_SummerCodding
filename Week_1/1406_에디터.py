from sys import stdin
from collections import deque

left = deque(list(stdin.readline().strip()))
right = deque()

M = int(stdin.readline())
for i in range(M):
    str = stdin.readline()
    if str[0] == "L":
        if len(left) == 0:
            continue
        right.appendleft(left.pop())
    elif str[0] == "D":
        if len(right) == 0:
            continue
        left.append(right.popleft())
    elif str[0] == "B":
        if len(left) == 0:
            continue
        left.pop()
    else:
        left.append(str[2])

print("".join(left + right))
