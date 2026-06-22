n = int(input())

intervals = []
res = []

for i in range(n):
    l, r = map(int, input().split())
    intervals.append([l, r])

intervals.sort(key = lambda x : x[0])

begin = end = -2e9

for interval in intervals:
    if end < interval[0]:
        if begin != -2e9:
            res.append([begin, end])
        begin = interval[0]
        end = interval[1]
    else:
        end = max(end, interval[1])

if begin != -2e9:
    res.append([begin, end])

print(len(res))
