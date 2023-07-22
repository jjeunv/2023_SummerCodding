import sys, itertools

input = sys.stdin.readline

n, m, k = map(int, input().split())

skills = []
skill = []


def cal(q):
    cnt = 0
    for i in skills:
        flag = 1
        for j in i:
            if not j in q:
                flag = 0
                break
        if flag == 1:
            cnt += 1
    return cnt


for i in range(m):
    s = list(map(int, input().strip().split()))
    skills.append(s)

for i in range(1, 2 * n + 1):
    skill.append(i)

max_num = 0

for i in itertools.combinations(skill, n):
    quest_num = cal(i)
    if max_num < quest_num:
        max_num = quest_num

print(max_num)
