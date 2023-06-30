N=int(input())
book={}
while N>0 :
    key=input()
    if key in book :
        book[key]=book[key]+1
    else:
        book[key]=1
    N-=1

book = dict(sorted(book.items(),key=lambda x: (-x[1],x[0])))
print(next(iter(book)))