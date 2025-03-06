import re

string="Hello, World!"
pattern="Hello, \w+!"
matches=re.match(pattern, string)
print(matches)
