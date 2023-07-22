import sys

input = sys.stdin.readline

N = int(input())

cnt = 0

# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0

l = [-1] * N


# 0 2 -1 -1
def check(x):
    # print(l)
    for i in range(x):  # 0 1
        if l[i] == l[x] or abs(l[i] - l[x]) == abs(i - x):
            # print(l)
            return False
    # print(l)
    return True


def nqueen(x):
    global cnt
    if x == N:
        cnt += 1
        # print(l,cnt)
        return

    for i in range(N):
        l[x] = i  # (x,i)
        if check(x):
            nqueen(x + 1)


nqueen(0)
print(cnt)
