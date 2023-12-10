def extgcd(a, b):
    if b != 0:
        c, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return c, x, y
    return a, 1, 0


def modpow(a, b, m):
    ans = 1
    while 0 < b:
        if b & 1 == 1:
            ans = (ans * a) % m
        a = (a * a) % m
        b >>= 1
    return ans


def divisor(n):
    for i in range(2, int(n ** (1 / 2))):
        if n % i == 0:
            p = i
            q = n // i
            return p, q


n, e, E = map(int, input().split())
p, q = divisor(n)
n_prime = (p - 1) * (q - 1)

c, x, y = extgcd(e, n_prime)
d = (x + n_prime) % n_prime
M = modpow(E, d, n)

print(M)
print(bin(M))


letter = [0] * 4
for i in range(4):
    for j in range(7):
        if M % 2 == 1:
            letter[i] += pow(2, j)
        M //= 2

print(letter)

output = ""
for i in range(4):
    if letter[3 - i] != 0:
        output += chr(letter[3 - i])
print(output)
"""
ans_str = ""

for i in range(2, 24, 7):
    str_code_bin = str(bin(M))[i:i+7]
    if str_code_bin != "0000000":
        print(int(str_code_bin, 2))
        ans_str += chr(int(str_code_bin, 2))

print(ans_str
"""