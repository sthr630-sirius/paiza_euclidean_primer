import math
def get_pq(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return i
def extgcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, g = extgcd(b, a%b)
        X = y
        Y = x - a//b * y
        return X, Y, g
def modpow(a, b, n):
    ans = 1
    while b>0:
        if b&1:
            ans = (ans*a)%n
        b >>= 1
        a = (a*a)%n
    return ans

n, e, E = map(int, input().split())
p = get_pq(n)
q = n//p
n_prime = (p-1)*(q-1)
d, y, g = extgcd(e, n_prime)
d = d%n_prime

m = modpow(E, d, n)
ans_bin = str(bin(m))[2:].zfill(28)
ans_str = ""

for i in range(0, 22, 7):
    ans_chr_bin = ans_bin[i:i+7]
    if ans_chr_bin != "0000000":
        #print(int(str_code_bin, 2))
        ans_str += chr(int(ans_chr_bin, 2))

print(ans_str)