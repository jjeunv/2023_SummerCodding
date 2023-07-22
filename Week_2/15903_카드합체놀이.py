from sys import stdin  

n,m=map(int,stdin.readline().split())

card=list(map(int,stdin.readline().split()))

for i in range(m):   
    card.sort()    
    card[0]=card[0]+card[1]
    card[1]=card[0]

print(sum(card))
