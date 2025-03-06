array_values=[10, 20, 60, 30, 90]
element_to_find=30

index=-1
for i, value in enumerate(array_values):
 if value==element_to_find:
  index=i
  break

print(index)
