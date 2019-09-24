# [My Python Practice]


## Generate_Limited_Range_ND.py (2019.09.22)
- partial module of a gaming utility for `Romance of The Three Kingdoms II` (KOEI, 1989)
- generate `rate` data for practicing `gold`-`food` arbitrage

#### Method 0. Generating initial data (not trimmed yet)
```python
mu, sigma, n = 50, 10, 1000
llimit, rlimit = 25, 75

data = np.random.normal(mu, sigma, n)
```
```python
plt.hist(data)
stats.describe(data)[0:2] # [0] : nobs, [1] : minmax
```
![hist0](https://github.com/kimpro82/My_Practice/blob/master/images/Generate_Limited_Range_ND_hist_0.png)
> (1000, (16.763171096395133, 76.969552776105601))

#### Method 1. Trim with rack of amount
```python
data1 = data[(data >= llimit) & (data <= rlimit)]
```
```python
plt.hist(data1)
stats.describe(data1)[0:2]
```
![hist1](https://github.com/kimpro82/My_Practice/blob/master/images/Generate_Limited_Range_ND_hist_1.png)
> (991, (25.600374595125377, 74.942171158969671))

#### Method 2. Check each one trial
```python
data2, amount = [], 0

while amount < n :
    data_temp = np.random.normal(mu, sigma, 1)
    if (data_temp >= llimit) & (data_temp <= rlimit) :
        data2 = np.append(data2, data_temp)
        amount += 1
```
```python
plt.hist(data2)
stats.describe(data2)[0:2]
```
![hist2](https://github.com/kimpro82/My_Practice/blob/master/images/Generate_Limited_Range_ND_hist_2.png)
> (1000, (25.987274047611137, 73.473315070409228))

#### Method 3. Generate one round and fill the lack
```python
data3 = data[(data >= llimit) & (data <= rlimit)]
amount = len(data3)

while amount < n :
    data_temp = np.random.normal(mu, sigma, 1)
    if (data_temp >= llimit) & (data_temp <= rlimit) :
        data3 = np.append(data3, data_temp)
        amount += 1
```
```python
plt.hist(data3)
stats.describe(data3)[0:2]
```
![hist3](https://github.com/kimpro82/My_Practice/blob/master/images/Generate_Limited_Range_ND_hist_3.png)
> (1000, (25.600374595125377, 74.942171158969671))

## RTK2_CallData_Pandas.py (2019.08.12)
- partial module of a gaming utility for `Romance of The Three Kingdoms II` (KOEI, 1989)
- upgrade : adopt `Numpy` & `Pandas` and convert to a `class`
- The parameter `lord` of the def `dataload` doesn't work yet.
- The columns aren't named yet, too.

```python
# Class using NumPy & Pandas
import numpy as np
import pandas as pd

class Rtk2 :

    # province_offset_data
    def __init__(self) :
        self.province_offset_init = []
        self.province_offset_data = []

        for i in list(range(0,41)) :
            self.province_offset_init.append(11668 + 35*i)
            self.province_offset_data.append(list(range(self.province_offset_init[i], self.province_offset_init[i]+35)))

    # call the save data on each offset location
    def dataload(self, path, lord) :
        self.path = path
        self.lord = lord

        with open(self.path,'rb') as self.f:
            self.province_law_data = self.f.read()
            self.province_data = []

            for i in list(range(0,41)) :
                self.province_data_row = []

                for j in list(range(0,35)) :    
                    self.province_data_row.append(self.province_law_data[self.province_offset_data[i][j]])
                self.province_data.append(self.province_data_row)

        self.province_data_array = np.array(self.province_data)

        # calculate pop, gold and food
        self.province_pop = []
        self.province_gold = []
        self.province_food = []

        for i in list(range(0,41)) :
            self.province_pop.append((self.province_data_array[i][6] + self.province_data_array[i][7]*(2**8))*100)
            self.province_gold.append(self.province_data_array[i][0] + self.province_data_array[i][1]*(2**8))
            self.province_food.append(self.province_data_array[i][2] + self.province_data_array[i][3]*(2**8) + self.province_data_array[i][4]*(2**16))

        # merge the dataframes
        self.province_gold_array = pd.DataFrame(self.province_gold, columns=['Gold'])
        self.province_food_array = pd.DataFrame(self.province_food, columns=['Food'])
        self.province_pop_array = pd.DataFrame(self.province_pop, columns=['Pop'])

        self.province_data_df = pd.DataFrame(self.province_data)

        return pd.concat([
                self.province_pop_array,
                self.province_gold_array,
                self.province_food_array,
                self.province_data_df.iloc[:, 8],
                self.province_data_df.iloc[:, 14:20]
                ],
                axis=1)
```

```python
rtk2 = Rtk2()

save = rtk2.dataload('path', 15) # the parameter lord('15') doesn't work yet
save.head()
```

> Pop   Gold     Food   8   14   15   16  17  18  19  
> 0  274400   4080     4364   3    9   75    4   4   1  27  
> 1  225900  29450  2700000  15   50  100   92   0   2  62  
> 2  253300  29950  2700000  15  100  100  100  28   4  70  
> 3  198500  30000  2699000  15  100  100  100  79   0  66  
> 4  268000  30000  2700000  15  100  100  100  16   1  48  


## RTK2_CallData.py (2019.07.23)
- partial module of a gaming utility for `Romance of The Three Kingdoms II` (KOEI, 1989)
- call each province's data of population, gold, food and so on from a save file

```python
# province_offset_data - from RTK2_Offset.py (2019.07.22)
province_offset_init = []
province_offset_data = []

for i in list(range(0,41)) :
    province_offset_init.append(11668 + 35*i)
    province_offset_data.append(list(range(province_offset_init[i], province_offset_init[i]+35)))
```

```python
# call the save data on each offset location
with open('Documents/신랑/개발/Python/SAVE','rb') as f:
    province_law_data = f.read()
    province_data = []
    
    for i in list(range(0,41)) :
        province_data_row = [] 
        for j in list(range(0,35)) :    
            province_data_row.append(province_law_data[province_offset_data[i][j]])
        province_data.append(province_data_row)

print(province_data[0:3])
```
> [[182, 0, 8, 1, 0, 0, 240, 9, 3, 255, 128, 48, 255, 255, 7, 79, 4, 4, 1, 34, 8, 1, 55, 0, 6, 0, 0, 196, 45, 217, 0, 0, 0, 0, 0],  
> [20, 10, 172, 74, 4, 0, 20, 9, 3, 255, 128, 50, 255, 2, 56, 100, 52, 0, 2, 64, 221, 0, 67, 0, 5, 0, 0, 150, 46, 11, 26, 12, 5, 0, 0],  
> [48, 117, 96, 54, 42, 0, 61, 9, 15, 255, 0, 0, 255, 255, 100, 99, 100, 33, 4, 55, 174, 0, 73, 0, 4, 1, 0, 0, 0, 182, 4, 0, 0, 0, 0]]

```python
# test : gold
province_gold = []

for i in list(range(0,41)) :
    province_gold.append(province_data[i][0] + province_data[i][1]*256)

print(province_gold)
```
> [182, 2580, 30000, 30000, 30000, 7139, 30000, 1783, 29880, 30000, 29988, 30000, 130, 73, 51, 339, 30000, 0, 30000, 11841, 311, 2542, 12033, 0, 100, 100, 100, 605, 3697, 8908, 30000, 22452, 30000, 6341, 7482, 3649, 2528, 574, 4451, 8050, 12206]

```python
# all province data
province_gold = []
province_food = []
province_pop = []
province_rate = []
province_horses = []
province_loy = []
province_land = []
province_flood = []
province_forts = []

for i in list(range(0,41)) :
    province_gold.append(province_data[i][0] + province_data[i][1]*(2**8))
    province_food.append(province_data[i][2] + province_data[i][3]*(2**8) + province_data[i][4]*(2**16))
    province_pop.append((province_data[i][6] + province_data[i][7]*(2**8))*100)
    province_rate.append(province_data[i][19])
    province_horses.append(province_data[i][17])
    province_loy.append(province_data[i][15])
    province_land.append(province_data[i][14])
    province_flood.append(province_data[i][16])
    province_forts.append(province_data[i][18])

print("Province", "Pop\t\t", "Gold\t", "Food\t\t", "Rate Horses Loy Land Flood Forts")
for i in list(range(0,10)) :
    print(i+1, "\t", province_pop[i], "\t", province_gold[i], "\t", province_food[i], "\t", end =' ')
    print(province_rate[i], province_horses[i], province_loy[i], province_land[i], province_flood[i], province_forts[i])
```
> Province Pop             Gold    Food            Rate Horses Loy Land Flood Forts  
> 1        254400          182     264     34 4 79 7 4 1  
> 2        232400          2580    281260          64 0 100 56 52 2  
> 3        236500          30000   2766432         55 33 99 100 100 4  
> 4        179300          30000   1732260         46 82 99 93 96 0  
> 5        246800          30000   2666060         57 19 96 100 100 1  
> 6        499500          7139    233937          50 42 98 79 64 3  
> 7        269800          30000   2730580         37 85 94 100 100 3  
> 8        173600          1783    329476          41 49 100 83 83 2  
> 9        276300          29880   2694902         30 39 95 47 79 2  
> 10       1010800         30000   3000000         33 83 96 100 100 6  


## RTK2_Offset.py (2019.07.22)
- partial module of a gaming utility for `Romance of The Three Kingdoms II` (KOEI, 1989)
- make offset locations' list before call the save data

```python
"""
the initial data offset addresses of the each province (hexadecimal)
1 - 2d94
2 - 2db7   
3 - 2dda
……
41 - 330c
"""
```

```python
# 각 영토별 데이터는 35바이트 단위임을 확인
int('2db7', 16) - int('2d94', 16)
int('2dda', 16) - int('2db7', 16)
```
> 35  
> 35

```python
# 영토별 첫번째 값의 offset 위치를 10진수로 확인
0x2d94
0x330c
type(0x330c) # 이 자체로 int type
```
> 11668  
> 13068  
> int

```python
# 35바이트 간격 리스트 생성하기(*꼭 16진수로 할 필요없다)
province_offset_init = [11668]
for i in list(range(1,41)) :
    province_offset_init.append(province_offset_init[0] + 35*i)

print(province_offset_init)
len(province_offset_init)
```
> [11668, 11703, 11738, 11773, 11808, 11843, 11878, 11913, 11948, 11983, 12018, 12053, 12088, 12123, 12158, 12193, 12228, 12263, 12298, 12333, 12368, 12403, 12438, 12473, 12508, 12543, 12578, 12613, 12648, 12683, 12718, 12753, 12788, 12823, 12858, 12893, 12928, 12963, 12998, 13033, 13068]  
> 41

```python
# offset : gold
province_offset_gold = []
for i in list(range(0,41)) :
    province_offset_gold.append([province_offset_init[i], province_offset_init[i]+1])

print(province_offset_gold)
# offset : food
# offset : loyalty
# an so on …… 
```
> [[11668, 11669], [11703, 11704], [11738, 11739], [11773, 11774], [11808, 11809], [11843, 11844], [11878, 11879], [11913, 11914], [11948, 11949], [11983, 11984], [12018, 12019], [12053, 12054], [12088, 12089], [12123, 12124], [12158, 12159], [12193, 12194], [12228, 12229], [12263, 12264], [12298, 12299], [12333, 12334], [12368, 12369], [12403, 12404], [12438, 12439], [12473, 12474], [12508, 12509], [12543, 12544], [12578, 12579], [12613, 12614], [12648, 12649], [12683, 12684], [12718, 12719], [12753, 12754], [12788, 12789], [12823, 12824], [12858, 12859], [12893, 12894], [12928, 12929], [12963, 12964], [12998, 12999], [13033, 13034], [13068, 13069]]

```python
# province_offset_data (more efficient way)
province_offset_data = []
for i in list(range(0,41)) :
    province_offset_data.append(list(range(province_offset_init[i], province_offset_init[i]+35)))

print(province_offset_data[0:2])
```
> [[11668, 11669, 11670, 11671, 11672, 11673, 11674, 11675, 11676, 11677, 11678, 11679, 11680, 11681, 11682, 11683, 11684, 11685, 11686, 11687, 11688, 11689, 11690, 11691, 11692, 11693, 11694, 11695, 11696, 11697, 11698, 11699, 11700, 11701, 11702], [11703, 11704, 11705, 11706, 11707, 11708, 11709, 11710, 11711, 11712, 11713, 11714, 11715, 11716, 11717, 11718, 11719, 11720, 11721, 11722, 11723, 11724, 11725, 11726, 11727, 11728, 11729, 11730, 11731, 11732, 11733, 11734, 11735, 11736, 11737]]

```python
# province_offset_data (final)
province_offset_init = []
province_offset_data = []
for i in list(range(0,41)) :
    province_offset_init.append(11668 + 35*i)
    province_offset_data.append(list(range(province_offset_init[i], province_offset_init[i]+35)))

print(province_offset_init)
print(province_offset_data[0:2])
```
> [11668, 11703, 11738, 11773, 11808, 11843, 11878, 11913, 11948, 11983, 12018, 12053, 12088, 12123, 12158, 12193, 12228, 12263, 12298, 12333, 12368, 12403, 12438, 12473, 12508, 12543, 12578, 12613, 12648, 12683, 12718, 12753, 12788, 12823, 12858, 12893, 12928, 12963, 12998, 13033, 13068]  
> [[11668, 11669, 11670, 11671, 11672, 11673, 11674, 11675, 11676, 11677, 11678, 11679, 11680, 11681, 11682, 11683, 11684, 11685, 11686, 11687, 11688, 11689, 11690, 11691, 11692, 11693, 11694, 11695, 11696, 11697, 11698, 11699, 11700, 11701, 11702], [11703, 11704, 11705, 11706, 11707, 11708, 11709, 11710, 11711, 11712, 11713, 11714, 11715, 11716, 11717, 11718, 11719, 11720, 11721, 11722, 11723, 11724, 11725, 11726, 11727, 11728, 11729, 11730, 11731, 11732, 11733, 11734, 11735, 11736, 11737]]


## With_Open.py (2019.07.21)
- read binary file
- convert decimal number ↔ hexadecimal number

```python
# get current working directory
import os

os.getcwd()
print(os.getcwd())

# check if the file exists
os.path.isfile("path")
```
> True

```python
import binascii

# with문
with open('path','rb') as f: # rb : read & binary
    string = f.read()
    print(string[0:10])
    print(binascii.b2a_hex(string[0:10]))
```
> b'1990.02.19'  
> b'313939302e30322e3139'

```python
# with문 X
f = open('path','rb')
data = f.read()
print(data[0:10])
print(binascii.b2a_hex(data[0:10]))
f.close()
```
> b'1990.02.19'  
> b'313939302e30322e3139'

```python
# decimal → hexadecimal
hex(30000)
hex(3000000)
hex(100)
```
> '0x7530'  
> '0x2dc6c0'  
> '0x64'

```python
# hexadecimal → decimal
int('7530', 16)
int('2dc6c0', 16)
int('64', 16)
```
> 30000  
> 3000000  
> 100


## Password.py (2019.05.24)
input the correct passworld within 5 trials or die  
practice if~else, break/continue, time.sleep() and so on

```python
import time # for using time.sleep()

chance = 0
pw_original = "mymy" # password. a word that calls a pass. you nahm sayin?

while chance < 5 :
    pw_input = input("Input your password : ")

    # right
    if pw_original == pw_input :
        print("You entered the correct password")
        break
    
    # wrong
    else:
        chance += 1
        print("You entered the wrong passwords", chance, "times.")
        if chance == 5 :
            print("You bad guys will be delayed as a penalty.")
            time.sleep(3)
        else :
            continue

# Of course, saving the original password in this file is somewhat stupid.
# But, yes I am.
```


## Player (2019.03.12) - maybe?
A class that traces a player's coordinate

```python
# generating a player who has locatiion (a,b) and its trace data
 
 
class player :
    
    name = ''
    # can be named at each instance
    location = [0,0]
    # can be set as a random position (future task)
    trace = [[0,0]]
    # accumulationg as a list of location (a,b)s' trace
    
    def init(self, name, location, trace) : # Why doesn't __init__ work?
    # alternative : def init(self, name='', location=[0,0], trace=[])
        self.name = name
        self.location = location
        self.trace = trace
    
    # methods for moving
    def right(self, num=1) :
        self.location = [self.location[0] + num, self.location[1]]
        self.trace.append(self.location)
        print(self.location)
        # Is there any other way to avoid repeat this common line?
    
    def left(self, num=1) :
        self.location = [self.location[0] - num, self.location[1]]
        self.trace.append(self.location)
        print(self.location)
    
    def up(self, num=1) :
        self.location = [self.location[0], self.location[1] + num]
        self.trace.append(self.location)
        print(self.location)
    
    def down(self, num=1) :
        self.location = [self.location[0], self.location[1] - num]
        self.trace.append(self.location)
        print(self.location)
        
        # Should 'self' be really abused so much like the above?
```

```python
# generating an instance
p1 = player() 

# Results
p1.right()
p1.up(3)
p1.left(2)
print(p1.trace)
```
> [1, 0]  
[1, 3]  
[-1, 3]  
[[0, 0], [1, 0], [1, 3], [-1, 3]]  


## Class_Test.py (2018.02.07)
a simple Python `class` practice

```python
class MyFirstClass :
    
    def Family(self, name, role):
        print(name, "is a(an)", role, "in my family")

Do = MyFirstClass()

Do.Family("Kim", "Husband")
Do.Family("Shin", "Wife")
Do.Family("Kim", "Future Baby")
```

![Python_Class_Test](https://github.com/kimpro82/My_Practice/blob/master/images/2018-02-07%20Python_Class_Test.PNG)

I found that a simple `class` in Python doesn't need stuffs like `__main__`, `__init__` and so on.
What the `__hell__`?


## Nirvana.py (2017.05.15)
a simple Python practice

```python
death_entropy = 100
my_entropy = 1

while(my_entropy < death_entropy) :
    print(my_entropy)
    my_entropy += 1
print('Nirvana')
```
