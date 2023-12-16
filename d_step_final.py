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

send_message = "tttr"
send_message_bin = ""

for c in send_message:
    send_message_bin = send_message_bin + str(bin(ord(c)))[2:].zfill(7)

M = int(send_message_bin.ljust(28, "0"), 2)

print(send_message)

p = 23917
q = 23929
n = p*q
n_prime = (p-1)*(q-1)
e = 8731

print(f"n: {n}")
print(f"p: {p}")
print(f"q: {q}")
print(f"n': {n_prime}")
print(f"e: {e}")

d, y, g = extgcd(e, n_prime)
d = d%n_prime

print(f"gcd(e, n')={g}")
print(f"d:", d)
print(f"de= {d*e%n_prime} mod(n')")

E = modpow(M, e, n)
print(f"M:", M)
print(f"E:", E)
decode_M = modpow(E, d, n)
print(f"deM:", decode_M)

ans_bin = str(bin(decode_M))[2:].zfill(28)
print(ans_bin)
ans_str = ""

for i in range(0, 22, 7):
    ans_chr_bin = ans_bin[i:i+7]
    if ans_chr_bin != "0000000":
        ans_str += chr(int(ans_chr_bin, 2))

print(ans_str)