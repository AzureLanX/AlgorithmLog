n, m = map(int, input().split())
data = [0] + list(map(int, input().split()))

diff = [0] * (n+2)

for i in range(n):
    diff[i+1] = data[i+1] - data[i]

for i in range(m):
    l, r, c = map(int, input().split())
    diff[l] += c
    diff[r+1] -= c

for i in range(n):
    diff[i+1] = diff[i] + diff[i+1]
    print(diff[i+1], end=" ")

