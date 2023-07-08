from sys import stdin
from collections import deque

N, W, L = map(int, stdin.readline().split())  # 4 2 10

truck = deque(list(map(int, stdin.readline().split())))
bridge = deque(maxlen=W)
cnt = 0

while bridge.count(0) != W:
    if len(truck) != 0:
        if len(bridge) == W:
            bridge.popleft()
        if sum(bridge) + truck[0] <= L:
            bridge.append(truck.popleft())
            cnt += 1
        else:
            bridge.append(0)
            cnt += 1
    else:
        bridge.append(0)
        cnt += 1

print(cnt)
