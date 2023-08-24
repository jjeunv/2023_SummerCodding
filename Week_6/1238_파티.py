import sys
import heapq

INF=1e9

input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [[] for i in range(N + 1)]

for i in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))


def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance=[INF] *(N+1)
    distance[start]=0

    while q:
        dist,cur=heapq.heappop(q)

        if distance[cur]<dist:
            continue

        for i in graph[cur]:
            weight=dist+i[1]
            if weight<distance[i[0]]:
                distance[i[0]]=weight
                heapq.heappush(q,(weight,i[0]))
    
    return distance


answer=0
start_x=dijkstra(X)

for i in range(1,N+1):
    start_i=dijkstra(i)

    
    #print(start_i)
    #print(start_x[X],start_i[i])
    answer=max(answer,start_x[i]+start_i[X])

print(answer)
