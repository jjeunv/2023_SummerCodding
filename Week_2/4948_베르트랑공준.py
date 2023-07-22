from sys import stdin 
import math

def is_prime(x):

    prime=[True]*(2*x+1)

    for i in range(2,int(math.sqrt(2*x))+1):
        if prime[i]==True:
            for j in range(i*2,2*x+1,i):
                prime[j]=False
    
    cnt=0
    for i in range(x+1,2*x+1):
        if i==1:
            continue
        else:
            if prime[i]==True:
                cnt+=1
    
    print(cnt)
    

num=int(stdin.readline())
while num!=0:
    is_prime(num)
    num=int(stdin.readline())
