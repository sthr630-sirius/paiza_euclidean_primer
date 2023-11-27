def my_gcm(a, b):
    if b == 0:
        return a

    return my_gcm(b, a%b)

n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

a = num[0]

if n != 1:
    for i in range(1, n):
        p = max(a, num[i])
        q = min(a, num[i])
        a = my_gcm(p, q)

print(a)