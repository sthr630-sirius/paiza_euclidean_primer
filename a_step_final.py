def my_gcd(a, b):
    if b == 0:
        return a
    return my_gcd(b, a%b)

def my_euclidean(a, b):
    if b == 0:
        x = 1
        y = 0
        g = a
        print(f"a:{a} b:{b} x:{x} y:{y} g:{g}")
        print(f"{a} * {x} + {b} * {y} = {g}")
        print("")
        return x, y, g
    #print(f"{a} = {b} * {a//b} + {a%b}")
    x, y, g = my_euclidean(b, a%b)
    print(f"x:{x}, y:{y}")
    X = y
    Y = x - (a//b) * y
    print(f"a:{a} b:{b} x:{X} y:{Y} g:{g}")
    print(f"{a} * {X} + {b} * {Y} = {g}")
    print("")
    return X, Y, g

A, B = map(int, input().split())
#print(my_gcd(A,B))
x, y, g = my_euclidean(A, B)
print(x, y)