arr=[10, 20, 40, 10, 40, 10, 20]
dups=[]

for i in range(len(arr)):
 for j in range(i + 1, len(arr)):
  if arr[i]==arr[j] and arr[i] not in dups:
   dups.append(arr[i])

print(dups)
