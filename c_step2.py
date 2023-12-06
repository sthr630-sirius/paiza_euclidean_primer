n = int(input())
a, cal, b = input().split()
a = int(a)
b = int(b)
if cal == "+":
    a = a % n
    b = b % n
    print((a+b)%n)
elif cal == "-":
    a = a % n
    b = b % n
    print((a-b)%n)
elif cal == "*":
    a = a % n
    b = b % n
    print((a * b) % n)
elif cal == "^":
    a = a % n
    print((a**b) % n)