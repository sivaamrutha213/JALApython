def equal(a,b):
    a_str=str(a)
    b_str=str(b)
    if len(a_str)!=(b_str):
        return False
    for i in range(len(a_str)):
        if a_str[i]!=b_str[i]:
            return false
    return True
def not_equal(a,b):
    return not equal(a,b)
x=1234
y=1234
z=5678
print(equal(x,y))
print(equal(x,z))
print(not_equal(x,y))
print(not_equal(x,z))
