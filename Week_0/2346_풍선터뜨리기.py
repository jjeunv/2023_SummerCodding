from collections import deque

N=int(input())
size=N
dq=deque(maxlen=size)

l=list(map(int,input().split()))

num=1
for i in range(N):
    index_list=[l.pop(0),num]
    dq.append(index_list)
    num+=1

num_index=dq.popleft()
num=num_index[0]
index=num_index[1]
print(index,end=" ")
size-=1

while(size>0):
    if(num>0):
        for i in range(num-1):
            dq.append(dq.popleft())
        num_index=dq.popleft()
        num=num_index[0]
        index=num_index[1]
        print(index,end=" ")
        
         
    else:
        for i in range(-(num)-1):
            dq.appendleft(dq.pop())
        num_index=dq.pop()
        num=num_index[0]
        index=num_index[1]
        print(index,end=" ")
    
    size-=1
