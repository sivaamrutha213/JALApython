def less_than(a,b):
    if a-b<0:
        return True
    else:
        return False
def less_than_or_equal(a,b):
    if a-b<=0:
        return True
    else:
        return False
def greater_than(a,b):
    if b-a<0:
        return True
    else:
        return False
def greater_than_or_equal(a,b):
    if b-a<=0:
        return True
    else:
        return False
num1=
num2=10
print(f"{num1}<{num2}:",less_than(num1,num2))
print(f"{num1}<={num2}:",less_than_or_equal(num1,num2))
print(f"{num1}>{num2}:",greater_than(num1,num2))
print(f"{num1}>={num2}:",greater_than_or_equal(num1,num2))
