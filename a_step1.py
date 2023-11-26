def cal_r(a, b):
    r = a%b
    return b, r

x, y = map(int, input().split())
a = max(x, y)
b = min(x, y)

while b != 0:
    a, b = cal_r(a, b)

print(a)