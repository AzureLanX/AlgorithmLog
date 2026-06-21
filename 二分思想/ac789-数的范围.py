n, m = map(int, input().split())
q = list(map(int, input().split()))

while m:
    x = int(input())
    
    l = 0
    r = n - 1
    while l < r:
        mid = l + r >> 1
        if q[mid] >= x:
            r = mid
        else:
            l = mid + 1
    
    if q[l] != x:
        print("-1 -1")
    else:
        print(l, end = " ")

        l = 0
        r = n - 1
        while l < r:
            mid = l + r + 1 >> 1
            if q[mid] <= x:
                l = mid
            else:
                r = mid - 1
        
        print(l)

    m -= 1

