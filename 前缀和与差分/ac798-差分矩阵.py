N = 1010
n, m, q = map(int, input().split())

data = [[0] * N for _ in range(N)]
diff = [[0] * N for _ in range(N)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        data[i+1][j+1] = row[j]

# 构造差分矩阵
for i in range(1,n+1):
    for j in range(1,m+1):
        diff[i][j] = data[i][j] - data[i-1][j] - data[i][j-1] + data[i-1][j-1]

for i in range(q):
    x1, y1, x2, y2, c = map(int, input().split())
    diff[x1][y1] += c
    diff[x2+1][y1] -= c
    diff[x1][y2+1] -= c
    diff[x2+1][y2+1] += c

# 恢复矩阵
for i in range(1, n+1):
    for j in range(1, m+1):
        diff[i][j] = diff[i][j]+ diff[i-1][j] + diff[i][j-1] - diff[i-1][j-1]
        print(diff[i][j], end=" ")
    print()

