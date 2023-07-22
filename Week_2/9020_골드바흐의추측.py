import sys 
import math 
input=sys.stdin.readline 

t=int(input())


def prime(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1 ):
        if x%i==0:
            return False 
    return True

# 2 3 5 7 -> 3 5, 2 7
# 8//2= 4
# 3=8-5

for i in range(t):
    n=int(input())
    num=n//2
    while n>0:
        if prime(num) and prime(n-num):
            print(num, n-num)
            break
        num-=1