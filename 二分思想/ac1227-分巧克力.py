def check(mid:int):
    res = 0
    for h, w in s:
        res += (h // mid) * (w // mid)
    if res >= k:
        return True
    return False


n, k = map(int, input().split())

s = []

for i in range(n):
    h, w = map(int,input().split())
    s.append([h, w])

l = 0
r = 100010

while l < r:
    mid = l + r + 1 >> 1
    if check(mid):
        l = mid
    else:
        r = mid - 1

print(l)


