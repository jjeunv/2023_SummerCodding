from sys import stdin 
from collections import deque

N,K=map(int,stdin.readline().split())
num=deque(list(stdin.readline().strip()))

q=deque(maxlen=len(num)-K)

num_size=len(num)
size=len(num)-K
for i in num:

    n=int(i)
    if len(q)==0:
        q.append(n)
        size-=1
    else:

        while len(q)>0 and q[-1]<n:
            if num_size-1==size:
                break
            q.pop()
            size+=1

        if size==0:
            if q[-1]<n:
                q.pop()
                q.append(n)
        else:
            q.append(n)
            size-=1
            num_size-=1

last=''.join(map(str,list(q)))
print(last)