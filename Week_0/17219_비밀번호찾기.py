from sys import stdin

N,M=map(int,stdin.readline().split())

password={}
address_list={}
while(N>0):
    N-=1
    address,password=map(str, stdin.readline().split())
    address_list[address]=password

while(M>0):
    M-=1
    address=str(input())
    print(address_list[address])


