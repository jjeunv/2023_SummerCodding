import sys,itertools

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))

P_list=[]
for i in itertools.permutations(A):
    sum=0
    for j in range(N-1):
        sum+=abs(i[j]-i[j+1])
    
    P_list.append(sum)

print(max(P_list))