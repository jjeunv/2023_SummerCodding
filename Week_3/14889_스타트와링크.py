import sys, itertools
from collections import deque

input = sys.stdin.readline

N = int(input())

stats = []
people = []
people_c = deque()

for i in range(1, N + 1):
    people.append(i)

for i in range(N):
    stats.append(list(map(int, input().strip().split())))

for i in itertools.combinations(people, N // 2):
    people_c.append(i)

cnt = 10000

#print(stats)
#print(people)
#print(people_c)

def cal(team):
    team_sum = 0
    for i in itertools.permutations(team, 2):
        team_sum += stats[i[0] - 1][i[1] - 1]
    return team_sum


for i in range(len(people_c) // 2):
    start = people_c.popleft()
    link = people_c.pop()
    sub = abs(cal(start) - cal(link))
    if sub < cnt:
        cnt = sub
    if cnt == 0:
        break

print(cnt)
