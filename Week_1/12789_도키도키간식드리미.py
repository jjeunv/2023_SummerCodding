from sys import stdin
from collections import deque

N = int(stdin.readline())  # 학생 수

current = deque(list(map(int, stdin.readline().split())))  # 현재 서있는 줄
order = deque()  # 순서대로 갈 수 있는 줄
line = deque()  # 한명씩 일렬로 설 수 있는 줄

i = 1
while current:
    if current[0] == i:
        order.append(current.popleft())
        i += 1

    elif len(line) != 0 and line[-1] == i:
        order.append(line.pop())
        i += 1

    else:
        line.append(current.popleft())

while line:
    if line[-1] != i:
        break
    else:
        order.append(line.pop())
        i += 1

if len(order) == N:
    print("Nice")
else:
    print("Sad")
