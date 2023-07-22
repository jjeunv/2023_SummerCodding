from sys import stdin 
import math
T = int(stdin.readline())

def find(m, n, x, y):
    num = x
    while num <= math.lcm(n,m):
        if (num - x) % m == 0 and (num - y) % n == 0:
            return num
        num += m
    return -1

for i in range(T):
    m, n, x, y = map(int,stdin.readline().rstrip().split())
    print(find(m, n, x, y))
