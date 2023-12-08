def extgcd(a, b):
    #print(a, b)
    if b == 0:
        return 1, 0, a
    else:
        x, y, g = extgcd(b, a%b)
        X = y
        Y = x - a//b*y
        return X, Y, g

m, a = map(int, input().split())
x, y, g = extgcd(m, a)
print(y%m)