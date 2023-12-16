def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
def lcm(a, b):
    return a*b//gcd(a, b)
def addition(a, b, c, d):
    bottom = lcm(b, d)
    top = a*lcm(b, d)//b + c*lcm(b, d)//d
    return top//gcd(top, bottom), bottom//gcd(top, bottom)
def subtraction(a, b, c, d):
    bottom = lcm(b, d)
    top = a*lcm(b, d)//b - c*lcm(b, d)//d
    return top//gcd(top, bottom), bottom//gcd(top, bottom)
def multiplication(a, b, c, d) :
    bottom = b * d
    top = a * c
    return top//gcd(top, bottom), bottom//gcd(top, bottom)
def division(a, b, c, d) :
    bottom = b * c
    top = a * d
    return top//gcd(top, bottom), bottom//gcd(top, bottom)

a, b, cal, c, d = input().split()
a, b, c, d = map(int, [a, b, c, d])
#print(a, b, c, d)
if cal == "+":
    n, d = addition(a, b, c, d)
elif cal == "-":
    n, d = subtraction(a, b, c, d)
elif cal == "*":
    n, d = multiplication(a, b, c, d)
elif cal == "/":
    n, d = division(a, b, c, d)
print(n, d)