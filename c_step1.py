n, r = map(int, input().split())
max_n = 100000

i = 0
r = r%n
x = n * i + r

while x <= max_n:
    if x != 0:
        print(x)
    i += 1
    x = n * i + r
