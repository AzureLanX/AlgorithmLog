n, m = map(int, input().split())
data = list(map(int, input().split()))

a = [0] * (n+1)

for i in range(len(data)):
    a[i+1] = a[i] + data[i]

while m:
    l, r = map(int, input().split())
    res = a[r] - a[l-1]
    print(res)
    m -= 1