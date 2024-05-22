lst1 = input().split()
lst2 = input().split()
n = int(lst1[0])
k = int(lst1[1])
ans = 0
c = int(lst2[k-1])
for i in range(n):
    if int(lst2[i]) >= c and int(lst2[i]) != 0:
        print(int(lst2[i]), c)
        ans += 1
print(ans)