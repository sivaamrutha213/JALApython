f='C:\\my backup\\Programming\\JALA Python\\11.Files\\README.txt'  
pos=int(input("Enter position to start reading: "))

with open(f, 'r') as fl:
    fl.seek(pos)
    c=fl.read()

print(c)
