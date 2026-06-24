N = 100010
head = -1
idx = 0
e = [0] * N
ne = [0] * N

# 将x插入到头节点
def add_to_head(x:int):
    global idx, head
    e[idx] = x
    ne[idx] = head
    head = idx
    idx += 1

# 将x插到下标是k的后面
def add(k:int, x:int):
    global idx
    e[idx] = x
    ne[idx] = ne[k]
    ne[k] = idx
    idx += 1

# 将下标是K后面的点删除
def remove(k:int):
    ne[k] = ne[ne[k]]



m = int(input())

for s in range(m):
    op = input().split()
    if op[0] == 'H':
        x = int(op[1])
        add_to_head(x)
    elif op[0] == 'D':
        k = int(op[1])
        if k == 0:
            head = ne[head]
        else:
            remove(k-1)
    else:
        k = int(op[1])
        x = int(op[2])
        add(k-1, x)

# 遍历
i = head
while i != -1:
    print(e[i], end = " ")
    i = ne[i]

