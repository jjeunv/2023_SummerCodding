from sys import stdin
from collections import deque

N = int(stdin.readline())
top_list = deque(list(map(int, stdin.readline().split())))


q = []

for i in range(N):
    height=[]
    height.append(top_list.popleft())
    height.append(i+1)

    #print(height)
    #print(q)
    if len(q) == 0:
        q.append(height)
        print(0,end=" ")
    else:
        while len(q) != 0 and q[-1][0] <= height[0]:
            q.pop()
        q.append(height)
        if height==q[0]:
            print(0,end=" ")
        else:
            print(q[-2][1],end=" ")
    #print(q)

