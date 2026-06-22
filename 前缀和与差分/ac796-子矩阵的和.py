n, m, q = map(int, input().split())
data = [[0] * (m+1) for _ in range(n+1)]
prefix = [[0] * (m+1) for _ in range(n+1)]

for i in range(n):
    data[i+1] = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = data[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

while q:
    x1, y1, x2, y2 = map(int, input().split())
    res = prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]
    print(res)

    q -= 1