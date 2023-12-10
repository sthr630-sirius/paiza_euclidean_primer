def modpow(a, b, n):
    ans = 1
    while b > 0:
        if b&1:
            ans = (ans*a)%n
        b >>= 1
        a = (a*a)%n
    return ans

def extgcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, g = extgcd(b, a%b)
        X = y
        Y = x - a//b * y
        return X, Y, g

p, q, e, E = map(int, input().split())
n = p*q
n_prime = (p-1)*(q-1)
d, z, g = extgcd(e, n_prime)
d = d%n_prime
m = modpow(E, d, n)
print(chr(m))