from sys import stdin

N,P=map(int,stdin.readline().split())

guitar=[[] for i in range(7)]

count=0

while N>0:
    N-=1
    line,fret=map(int,stdin.readline().split())

    if(len(guitar[line])==0):
        guitar[line].append(fret)
        count+=1
        #print(guitar[line])
    else:
        if(fret>guitar[line][-1]):
            guitar[line].append(fret)
            count+=1
            #print(guitar[line])
        elif(fret<guitar[line][-1]):
            while(len(guitar[line])!=0 and fret<guitar[line][-1]):
                guitar[line].pop()
                count+=1
                #print(guitar[line])
            
            if(len(guitar[line])==0):
                guitar[line].append(fret)
                count+=1
            elif(fret!=guitar[line][-1]):
                guitar[line].append(fret)
                count+=1
                #print(guitar[line])


print(count)

    

