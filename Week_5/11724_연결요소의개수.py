import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]
visit = [False for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visit[v] = True
    for i in graph[v]:
        if not visit[i]:
            dfs(i)


cnt = 0

for i in range(1, n + 1):
    if not visit[i]:
        dfs(i)
        cnt+=1

print(cnt)
