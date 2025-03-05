def find_smaller_and_larger(a,b):
    if a-b<=0:
        smaller=a
        larger=b
    else:
        smaller=b
        larger=a
    return smaller,larger
num1=12
num2=23
smaller,larger=find_smaller_and_larger(num1,num2)#when input is given by user
print(f"The smaller number is:{smaller}")
print(f"The larger number is:{larger}")
