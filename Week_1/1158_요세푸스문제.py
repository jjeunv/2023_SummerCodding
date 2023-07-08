from collections import deque
from sys import stdin

# 1 2 3 4 5 6 7

N, K = map(int, stdin.readline().split())  # 7 3

P = []

i = 1
while i <= N:
    P.append(str(i))
    i += 1

P = deque(P)

l = []

while P:
    for i in range(K - 1):
        P.append(P.popleft())
    l.append(P.popleft())

l = "<" + ", ".join(l) + ">"
print(l)
print(l)
