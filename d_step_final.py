"""
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
"""
"""
send message : s = "test"
t --ord--> ord(t)=116 ---bin--> bin(116)=111 0100 ---zfill--> zfill(7)
e --ord--> ord(e)=101 ---bin--> bin(101)=110 0101 ---zfill--> zfill(7)
s --ord--> ord(s)=115 ---bin--> bin(115)=111 0011 ---zfill--> zfill(7)
t --ord--> ord(t)=116 ---bin--> bin(116)=111 0100 ---zfill--> zfill(7)

send_message -> send_message_bin -> int(send_message_bin, 2) = M
E = M^e mod n

p = 23917
q = 23929
n = p*q
n_prime = (p-1) * (q-1)
gcd(e, n_prime) = 1
"""

def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extgcd(b, a%b)
        u = y
        v = x - a//b * y
        return g, u, v

def modpow(a, n, mod):
    ans = 1
    while n>0:
        if n&1:
            ans = (ans*a) % mod
        n >>= 1
        a = (a*a) % mod

    return ans

p = 10000253
q = 10000261
n = p*q

"""
p' = p-1
q' = q-1
n' = p' * q'
"""
p_prime = p-1
q_prime = q-1
n_prime = p_prime * q_prime

"""
e : gcd(e, n') = 1
d : e^{-1} (mod n) --> e * d ≡ 1 (mod n') --> e * x + n' * y = 1 
"""
e = 7
g, d, y = extgcd(e, n_prime)
d = d%n_prime
print(f"g:{g}")
print(f"d:{d}")
"""
send_message = abcd
a --> ASCⅡコード：97 --> 0b1100001 = s0
b --> ASCⅡコード：98 --> 0b1100010 = s1
c --> ASCⅡコード：99 --> 0b1100011 = s2
d --> ASCⅡコード：100 --> 0b1100100 = s3
send_message_bin = s0 + s1 + s2 + s3 = 1100001 1100010 1100011 1100100 
send_message_int = 0b1100001110001011000111100100 = 205042148 --> M
"""
send_message = "abcd"
send_message_bin = ""
for i in range(4):
    send_message_bin += format(ord(send_message[i]), '07b')
send_message_int = int(send_message_bin, 2)
M = send_message_int
"""
E = M^e (mod n) 
"""
E = modpow(M, e, n)
print(send_message)
print(f"M:{M}")
print(f"n:{n}, e:{e}, E:{E}")
print(f"decode:{modpow(E, d, n)}")