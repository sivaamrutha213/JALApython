def arithmetic_operations(a,b,operation):
    if operation=="+":
        return a+b
    elif operation=="-":
        return a-b
    elif operation=="*":
        return a*b
    elif operation=="/":
        if b!=0:
            return a/b
        else:
            return "error"
    else:
        return "invalid operation"
a=10
b=20
print("addition",arithmetic_operations(a,b,"+"))
print("subtration",arithmetic_operations(a,b,"-"))
print("multiplication",arithmetic_operations(a,b,"*"))
print("Division",arithmetic_operations(a,b,"/"))
print("invaid operation",arithmetic_operations(a,b,"%"))
