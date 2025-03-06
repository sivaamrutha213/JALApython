arr=[10, 20, 30, 40, 50]
first_largest=float('-inf')
second_largest=float('-inf')

for num in arr:
 if num>first_largest:
  second_largest=first_largest
  first_largest=num
 elif num>second_largest and num!=first_largest:
  second_largest=num

print(second_largest)
