# [My Python Practice]

## RTK2_Offset.py (2019.07.22)
- partial module of a gaming utility for Romance of The Three Kingdoms (KOEI, 1989)
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
