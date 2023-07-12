from sys import stdin 
from collections import deque


N,K=map(int,stdin.readline().split()) 


coin=deque(maxlen=N)

for i in range(N):
    coin.append(int(stdin.readline()))

coin.reverse()
#print(coin)
cnt=0

for i in coin:
    #print(i)

    if i<=K:
        cnt+=K//i
        K=K%i
    

print(cnt)