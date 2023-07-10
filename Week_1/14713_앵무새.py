from sys import stdin 
from collections import deque
import copy

N=int(stdin.readline()) #앵무새 수
bird=dict()
index=0

while N>0:
    str=(stdin.readline().strip()).split(" ")
    bird[index]=deque(str)
    index+=1
    N-=1

str=deque((stdin.readline().strip()).split(" "))
b=bird

for i in str:
    cnt=0
    for j in b:
        if bird[j][0]==i:
            if len(bird[j])==1:
                bird.pop(j)
                cnt+=1
                break
            else:
                cnt=1
                bird[j].popleft()

                break
    if cnt==0:
        break

    # print(idx)

if cnt and len(bird)==0:
    print("Possible")
else:
    print("Impossible")