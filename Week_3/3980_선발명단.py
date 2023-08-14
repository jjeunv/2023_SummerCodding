import sys
input=sys.stdin.readline 

c=int(input())

while c>0:
    graph=[]
    for i in range(11):
        graph.append(list(map(int,input().strip().split())))

    l=[-1]*11

    def check(x,idx):
        for i in range(x):
            if l[x]==l[i]:
                return False
        if graph[idx][x]==0:
            return False
        return True
            
    
    maxnum=0
    def dfs(x):
        global maxnum
        if x==11:
            result=0
            for i in range(11):
                result+=graph[l[i]][i]
            maxnum=max(maxnum,result)
            return

        for i in range(11):
            l[x]=i
            if check(x,i):
                dfs(x+1)

    dfs(0)
    print(maxnum)
    
    c-=1