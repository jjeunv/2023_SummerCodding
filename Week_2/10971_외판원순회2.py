import sys
import itertools
input = sys.stdin.readline

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

ans = 10000000

order = [i for i in range(n)]


def sum_num(l):
    sum=0
    for i in range(n-1):
        if graph[l[i]][l[i+1]] == 0:
            return 0
        else:
            sum += graph[l[i]][l[i+1]]
    if graph[l[-1]][l[0]] != 0:
        sum += graph[l[-1]][l[0]]
    else:
        return 0
    return sum


for i in itertools.permutations(order):
    
    num=sum_num(i)
    if num!=0:
        ans=min(ans,num)

print(ans)