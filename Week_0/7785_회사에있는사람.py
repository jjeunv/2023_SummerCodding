from sys import stdin
n=int(stdin.readline())

commute_list={}
while(n>0):
    name, commute= map(str,stdin.readline().split())
    if commute=="leave":
        commute_list.pop(name)
    else :
        commute_list[name]=1
    n-=1

commute_list=dict(sorted(commute_list.items(), reverse=True))

s=""
for i in commute_list.keys():
    s+=(str(i)+'\n')
print(s)