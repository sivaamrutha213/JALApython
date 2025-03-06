
n=int(input())
s = 0
temp = n

while temp > 0:
    d = temp % 10
    s += d ** 3
    temp //= 10

if n == s:
    print("Armstrong")
else:
    print("Not Armstrong")
