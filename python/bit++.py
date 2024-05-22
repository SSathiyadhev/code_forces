n = int(input())
x = 0
for i in range(n):
    lin = input()
    if lin[0:2] == "++" or lin[1:3] == "++":
        x += 1
    elif lin[0:2] == "--" or lin[1:3] == "--":
        x -= 1
print(x)