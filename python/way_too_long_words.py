def short(w,s):
    n = len(w)
    if n <= 10:
        s.append(w)
    else:
        word = w[0]+str(n-2)+w[-1]
        s.append(word)

num = int(input())
lst = []
for i in range(num):
    wor = input()
    short(wor, lst)
for i in lst:
    print(i)
