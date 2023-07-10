from sys import stdin   

N,M=map(int,stdin.readline().split()) 

l=dict()
ls=[]
while N>0:
    name=stdin.readline().strip()
    l[name]=1
    N-=1

while M>0:
    name=stdin.readline().strip()
    if name in l:
        ls.append(name)
    M-=1

ls.sort()
print(len(ls))
for i in ls:
    print(i)