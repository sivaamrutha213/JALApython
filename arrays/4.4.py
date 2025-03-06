array_values=[10, 20, 30, 40, 50]
value_to_find=30

found=False
for value in array_values:
 if value==value_to_find:
  found=True
  break

print(found)
