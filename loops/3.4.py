start=1
end=20
print("Even numbers")
num=start
while(num//2)*2!=num:
    num+=1
while num<=end:
    print(num,end=" ")
    num+=2
print("\nOdd numbers:")
num=start
while(num//2)*2==num:
    num+=1
while num<=end:
    print(num,end=" ")
    num+=2
