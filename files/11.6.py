import os

f='C:\\my backup\\Programming\\JALA Python\\11.Files\\README.txt' 

r=os.access(f, os.R_OK)
w=os.access(f, os.W_OK)

print("Read access:", r)
print("Write access:", w)
