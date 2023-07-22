from sys import stdin 

n,m=map(int,stdin.readline().split())

def count_2(n):
    cnt=0
    x=2
    while x<=n:
        cnt+=n//x
        x*=2

    return cnt 

def count_5(n):
    cnt=0
    x=5
    while x<=n:
        cnt+=n//x
        x*=5

    return cnt 

# n!/(n-m)!*m!

cnt_2=count_2(n)-count_2(n-m)-count_2(m)
cnt_5=count_5(n)-count_5(n-m)-count_5(m)
print(min(cnt_2,cnt_5))
