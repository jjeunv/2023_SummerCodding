import sys
import heapq

input = sys.stdin.readline

INF = 1e9

n, m, r = map(int, input().split())

items = list(map(int, input().strip().split()))

graph = [[] for i in range(n + 1)]

for i in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))


def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
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

    item = 0
    for i in range(1, len(distance)):
        if distance[i] <= m:
            item += items[i - 1]

    return item


answer = 0

for i in range(1, n + 1):
    cur = dijkstra(i)
    answer = max(answer, cur)

print(answer)
