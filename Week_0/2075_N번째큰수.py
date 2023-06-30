from heapq import heappop, heappush

N= int(input())
index=N
num=[]

while(N>0):
    num_list=list(map(int,input().split()))
    if(len(num)==0):
        for i in range(len(num_list)):
            a=num_list.pop(0)
            heappush(num,a)
    else:
        for i in range(index):
            a=num_list.pop()
            if(num[0]<a):
                heappop(num)
                heappush(num,a)          
                
    N-=1

print(num[0])
