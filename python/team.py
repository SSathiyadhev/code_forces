n = int(input())
ans = 0
for i in range(n):
    s = input()
    if (s[0]== "1" and s[2]== "1") or (s[0]== "1" and s[4]== "1") or (s[2]== "1" and s[4]== "1"):
        ans += 1
print(ans)