import sys, itertools

input = sys.stdin.readline

n, k = map(int, input().split())
increment = list(map(int, input().strip().split()))

num = []

for i in range(1, n + 1):
    num.append(i)

cnt = 0


for i in itertools.permutations(num):
    
    weight = 500
    flag = True
    for j in range(n):
        weight += increment[i[j] - 1]
        weight -= k
        if weight < 500:
            flag = False
            break
    if flag:
        cnt += 1


print(cnt)
