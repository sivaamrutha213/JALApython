a=int(input("first number"))
b=int(input("second number"))
c=int(input("third number"))
largest=a
if b>=largest:
    largest=b
if c>largest:
    largest=c
print("the largest number is:",largest)
