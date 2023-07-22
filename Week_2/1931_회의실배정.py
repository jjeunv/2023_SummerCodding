from sys import stdin

n=int(stdin.readline())

room=[]

for i in range(n):
    l=list(map(int,stdin.readline().split()))
    room.append(l)

room.sort(key= lambda x: (x[1],x[0]))
#print(room)

cnt=1
num=room[0][1]
for i in range(1, n):
    
    if room[i][0]>=num:
        num=room[i][1]
        cnt+=1
    #print(room[i][0],num,cnt)
    
print(cnt)

    