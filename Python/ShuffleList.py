import random


# Trial 1

sufflelist = []

for i in range(0,20) :
    sufflelist.append(random.randint(1, 20))

print(sufflelist) # There are overlapping values.


# Trial 2

sufflelist = []

for i in range(0,20) :
    sufflelist.append(random.sample(range(1, 20), 1))

print(sufflelist)

# The values are in nested lists and overlapping ones still remains.


# Trial 3

list=[]

while len(list) < 10 :
    r = random.randint(1,100)
    if r not in list: list.append(r)

print(list) # There's no more overlapping values.
