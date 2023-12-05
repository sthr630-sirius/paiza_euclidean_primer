def my_gcm(a, b):
    if b == 0:
        return a

    return my_gcm(b, a%b)

a, b = map(int, input().split())

print((a*b)//my_gcm(a, b))