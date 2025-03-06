def remove_element(arr, value):
 arr.remove(value)
 return arr

array_values=[10, 20, 30, 40, 50]
value_to_remove=20

result=remove_element(array_values, value_to_remove)
print(result)
