from sys import stdin 
import heapq

N= int(stdin.readline()) # 정수의 개수 

left=[]  #maxheap
right=[]  #minheap

num =int(stdin.readline())
heapq.heappush(left,-num)
print(-left[0])

for i in range(N-1):
    num=int(stdin.readline())
    if len(left)>len(right):
        heapq.heappush(right,num)
    else:
        heapq.heappush(left,-num)
        
    
    if -left[0]>right[0]:
        n=-heapq.heappop(left)
        heapq.heappush(left,-heapq.heappop(right))
        heapq.heappush(right,n)
    # print(left,right)
    print(-left[0])
            

    

    #  1, 5, 2, 10, -99, 7, 5
    #         |  1  |
    #         |  1  | 5
    #      1  |  2  | 5
    #      1  |  2  | 5  10
    #  -99 1  |  2  | 5  10
    #  -99 1  |  2  | 5  7  10 
    #  -99 1 2|  5  | 5  7  10

