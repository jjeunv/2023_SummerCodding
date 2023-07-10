from sys import stdin

N=int(stdin.readline()) 

asg=[]
score=0

while N>0:
    str=stdin.readline().strip()
    list=str.split(' ')
    #print(list)
    if list[0]=='1':
        if list[2]=='1':
            score+=int(list[1])
        else:
            asg.append([int(list[1]),int(list[2])-1])  #과제 받자마자 시작
    else :
        if len(asg)==0:
            N-=1
            continue
        cnt=asg.pop()
        if(cnt[1]==1):
            score+=cnt[0]
        else:
            cnt[1]-=1
            asg.append(cnt)
    #print(asg,list)
    N-=1

print(score)