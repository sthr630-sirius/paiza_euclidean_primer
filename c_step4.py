a, b, m = map(int, input().split())
ans = 1
while b > 0:
    if b&1:
        ans = (ans*a)%m
    b >>= 1
    a *= a

print(ans)
