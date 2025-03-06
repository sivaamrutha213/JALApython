arr=[10, 20, 35, 41, 52, 68, 74, 85, 96, 107]
even_count=0
odd_count=0

for num in arr:
 if num % 2 == 0:
  even_count += 1
 else:
  odd_count += 1

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
