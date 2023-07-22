import sys,itertools
from collections import deque 
input=sys.stdin.readline 

N=int(input())

num=list(map(int,input().strip().split()))

op=list(map(int,input().strip().split()))

operator=['+','-','*','/']

op_list=[]

def cal(num,operator):
    #print(operator)
    result=num[0]

    for i in range(1,len(num)):
        #print(i)
        p=operator.popleft()
        if p=='+':
            result+=num[i]
            #print(num[i],result)
        elif p=='-':
            result-=num[i]
        elif p=='*':
            result*=num[i]
            #print(num[i])
        else:
            if result>=0 and num[i]>=0:
                result=result//num[i]
            else:
                result=-(abs(result)//abs(num[i]))
        #print(result)

    return result 







for i in range(4):
    p=operator.pop(0)
    for j in range(op.pop(0)):
        op_list.append(p)


maxnum=-1000000000
minnum=10000000000

case=list(itertools.permutations(op_list))
case=list(set(case))
for i in case:
    result=cal(num,deque(i))
    maxnum=max(maxnum,result)
    minnum=min(minnum,result)

print(maxnum)
print(minnum)
