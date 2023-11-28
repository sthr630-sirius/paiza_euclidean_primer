def my_gcm(a, b):
    if b == 0:
        return a

    return my_gcm(b, a%b)

a, b = map(int, input().split())

p = max(a, b)
q = min(a, b)

print((p*q)//my_gcm(p, q))