import sys
import heapq

input = sys.stdin.readline

INF = 1e9

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]


for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue

        for i in graph[cur]:

            weight = dist + i[1]

            if weight < distance[i[0]]:
                distance[i[0]] = weight
                heapq.heappush(q, (weight,i[0]))

    return distance

result=dijkstra(1)

print(result[n])