import sys, itertools

input = sys.stdin.readline


def check(check_num, num):
    check_num = str(check_num[0]) + str(check_num[1]) + str(check_num[2])
    num = str(num)
    # print(check_num,num)
    strike, ball = 0, 0
    for i in range(3):
        if check_num[i] in num:
            if check_num[i] == num[i]:
                strike += 1
            else:
                ball += 1
    return strike, ball


N = int(input())

game = []
for i in range(N):
    game.append(list(map(int, input().strip().split())))

num = []
for i in range(1, 10):
    num.append(i)

cnt = 0
for i in itertools.permutations(num, 3):
    flag = True
    for j in game:
        strike, ball = check(i, j[0])
        # print(i, j, check(i, j[0]))
        if strike != j[1] or ball != j[2]:
            flag = False
            break
    if flag:
        cnt += 1

print(cnt)
