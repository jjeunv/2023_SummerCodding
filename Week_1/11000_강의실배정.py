from sys import stdin 
from collections import deque
import heapq

N=int(stdin.readline()) 

lecture=[]

for i in range(N):
    time=list(map(int,stdin.readline().split()))
    #print(time)
    lecture.append(time)

lecture.sort()
lecture=deque(lecture)
#print(lecture)

heap=[]

for i in range(N):
    s,t=lecture.popleft()
    if len(heap)==0:
        heapq.heappush(heap,t)
    else:
        if heap[0]<=s:
            heapq.heappop(heap)
            heapq.heappush(heap,t)
        else:
            heapq.heappush(heap,t)


print(len(heap))