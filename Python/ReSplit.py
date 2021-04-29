txt = 'one two/three.four'

# 1. string.split()
print(txt.split())                  # default : ' '
print(txt.split('/'))
# print(txt.split(' ').split('/'))    # Error

# 2. Regular Expression
import re
print(re.split("[ /.]", txt))       # Enter delimiters directly
print(re.split("\W", txt))          # \W = a-zA-Z0-9