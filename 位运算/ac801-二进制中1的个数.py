n = int(input())
data = list(map(int,input().split()))



for i in range(n):
    ans = 0
    num = data[i]
    while num:
        num -= num & (-num)
        ans += 1
    print(ans, end=' ')