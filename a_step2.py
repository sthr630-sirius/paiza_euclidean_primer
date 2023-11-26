def my_gcm(a, b):
    if b == 0:
        return a

    return my_gcm(b, a%b)

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))
print(num)

print(my_gcm(num[0], num[1]))