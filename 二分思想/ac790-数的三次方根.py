n = float(input())

l = -30.0
r = 30.0

while r - l > 1e-7:
    mid = (l + r) / 2
    
    k = mid * mid * mid
    if k >= n:
        r = mid
    else:
        l = mid

print(f"{l:.6f}")