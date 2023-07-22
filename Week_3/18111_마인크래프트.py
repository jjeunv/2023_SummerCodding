import sys
from collections import Counter

input = sys.stdin.readline

n, m, b = map(int, input().split())

ground = []

for i in range(n):
    ground += map(int, input().split())

min_h = min(ground)
max_h = max(ground)
block = sum(ground)

ground = Counter(ground)

min_time = 1000000000
height = -1

for i in range(min_h, max_h + 1):
    if block + b >= i * n * m:
        time = 0
        for key in ground:
            if key < i:
                time += (i - key) * ground[key]
            else:
                time += (key - i) * ground[key] * 2
        if min_time >= time:
            min_time = time
            height = i

print(min_time, height)
