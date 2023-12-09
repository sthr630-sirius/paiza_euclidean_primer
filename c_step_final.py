def extgcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, g = extgcd(b, a%b)
        X = y
        Y = x - (a//b)*y
        return X, Y, g

def modpow(a, b, n):
    ans = 1
    while b > 0:
        if b & 1:
           ans = (ans*a)%n
        b >>= 1
        a = (a*a)%n

    return ans

p, q, e, m = map(int, input().split())

n = p * q
n_prime = (p-1) * (q-1)

x, y, g = extgcd(e, n_prime)
d = x%n_prime

E = modpow(m, e, n)

decode_E = modpow(E, d, n)

print(d)
print(E)
print(decode_E)
