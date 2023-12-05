a, b, c = map(int, input().split())
if a%b == c:
    x = 1
    y = -(a//b)
elif b%a == c:
    x = -(b//a)
    y = 1
print(x, y)