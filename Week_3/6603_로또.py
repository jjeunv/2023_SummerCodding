import sys, itertools

input = sys.stdin.readline


while True:
    num_list = list(map(int, input().strip().split()))
    if num_list[0] == 0:
        break
    k = num_list.pop(0)

    for i in itertools.combinations(num_list, 6):
        for j in i:
            print(j, end=" ")
        print()

    print()
