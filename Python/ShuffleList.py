import random

sufflelist = []

# for i in range(0,20) :
#   sufflelist.append(random.randint(1, 20))

# print(sufflelist)

# for i in range(0,20) :
#     sufflelist.append(random.sample(range(1, 20), 1))

# print(sufflelist)


list=[]
while len(list) < 10 :
    r = random.randint(1,100)
    if r not in list: list.append(r)

print(list)
