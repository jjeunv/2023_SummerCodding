import sys
import heapq

INF=1e9

input=sys.stdin.readline

n,e=map(int,input().split())

graph=[[] for i in range(n+1)]

for i in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2=map(int,input().split())

def dijkstra(start):
    q=[]
    distance=[INF]*(n+1)
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,cur=heapq.heappop(q)
        if dist<distance[cur]:
            continue
        for i in graph[cur]:
            weight=dist+i[1]
            if weight<distance[i[0]]:
                distance[i[0]]=weight
                heapq.heappush(q,(weight,i[0]))

    return distance

dist_v1=dijkstra(v1)
dist_v2=dijkstra(v2)
dist_start=dijkstra(1)

case_1=dist_start[v1]+dist_v1[v2]+dist_v2[n]
case_2=dist_start[v2]+dist_v2[v1]+dist_v1[n]

answer=min(case_1,case_2)

if answer>=INF:
    print(-1)
else:
    print(answer)