n =int(input())
p = True

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            p = False
            break
else:
    p = False

if p:
    print("Prime")
else:
    print("Not Prime")
