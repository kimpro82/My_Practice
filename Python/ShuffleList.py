import random


# Trial 1 : Use random.randint()

sufflelist = []

for i in range(0,20) :
    random.seed(330 + i)
    sufflelist.append(random.randint(1, 20))

print(sufflelist) # There are overlapping values.


# Trial 2 : Use random.sample()

sufflelist = []

for i in range(0,20) :
    random.seed(330 + i)
    sufflelist.append(random.sample(range(1, 20), 1))

print(sufflelist)

# The values are in nested lists and overlapping ones still remains.


# Trial 3 : Use While Statement

list=[]
loopnum = 0

while len(list) < 20 :
    random.seed(330 + loopnum)
    r = random.randint(1,20)
    if r not in list: list.append(r)
    loopnum += 1

print(list) # There's no more overlapping values.
print(loopnum) # It shows how many times overlapping numbers are rejected.
