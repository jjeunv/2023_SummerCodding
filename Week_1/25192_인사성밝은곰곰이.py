from sys import stdin

N = int(stdin.readline())
cnt = 0

chat = dict()

for i in range(N):
    name = str(stdin.readline().strip())
    if name == "ENTER":
        chat.clear()
        continue
    if name in chat:
        continue
    else:
        chat[name] = 1
        cnt += 1
print(cnt)
