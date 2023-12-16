def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

is_ans_exist = False

b_max = 1000
n, a = map(int, input().split())
for b in range(1, b_max):
    if n%gcd(a, b) != 0 and a != b:
        print(b)
        is_ans_exist = True

if not is_ans_exist:
    print(-1)