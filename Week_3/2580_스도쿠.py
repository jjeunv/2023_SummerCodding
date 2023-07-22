def is_valid(x, y, num):

    for i in range(9):
        if graph[x][i] == num or graph[i][y] == num:
            return False
    start_row, start_col = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if graph[start_row + i][start_col + j] == num:
                return False
    return True

def solve(n):
    if n==len(blank):
        for i in graph:
            print(*i)
        exit(0)
    for i in range(1,10):
        x=blank[n][0]
        y=blank[n][1]
        if is_valid(x,y,i):
            graph[x][y]=i
            solve(n+1)
            graph[x][y]=0


import sys 
input=sys.stdin.readline 

graph=[]
blank=[]

for x in range(9):
    graph.append(list(map(int,input().strip().split())))
    for y in range(9):
        if graph[x][y]==0:
            blank.append([x,y])

solve(0)
