from sys import stdin
import math

M = int(stdin.readline())
N = int(stdin.readline())

prime = [True] * (N + 1)

prime_list = []


for i in range(2, int(math.sqrt(N))+1):
    #print(i)
    if prime[i] == True:
        for j in range(i * 2, N + 1, i):
            prime[j] = False
            #print(i,j)

for i in range(M, N + 1):
    if i == 1:
        continue
    else:
        if prime[i] == True:
            prime_list.append(i)

#print(prime_list)
if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list), prime_list[0])
