from sys import stdin

str = str(stdin.readline().strip())
stick = []

sum = 0

stick.append(str[0])

i = 1
while i < len(str):
    if str[i] == "(":
        stick.append(str[i])

    else:
        if str[i - 1] == "(":
            stick.pop()
            sum += len(stick)
        else:
            stick.pop()
            sum += 1
    i += 1

print(sum)
