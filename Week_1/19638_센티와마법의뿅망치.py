from sys import stdin
import heapq


N,H,T=map(int,stdin.readline().split())
height=[]

while N>0:
    h=-int(stdin.readline())
    heapq.heappush(height,h)
    N-=1

cnt=0

#print(-height[0])
while -height[0]>=H:

    if -height[0]==1 or cnt>=T:
        break
    else:
        h=-(-heapq.heappop(height)//2)
        heapq.heappush(height,h)
        cnt+=1
    

if -height[0]>=H:
    print("NO")
    print(-height[0])
else:
    print("YES")
    print(cnt)
