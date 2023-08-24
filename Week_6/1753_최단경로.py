import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())

K = int(input())

INF = 1e8

graph = [[] for i in range(V + 1)]

distance = [INF] * (V + 1)

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


q = []


def dijkstra(start):
    heapq.heappush(q, (0, start))  # (우선순위, 값)
    distance[start] = 0

    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue

        for i in graph[cur]:
            weight = dist + i[1]
            if weight < distance[i[0]]:
                distance[i[0]] = weight
                heapq.heappush(q, (weight, i[0]))


dijkstra(K)

#print(distance)

for i in range(1, len(distance)):

    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
