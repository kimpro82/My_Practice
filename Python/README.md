# [My Python Practice]


## Generate_Limited_Range_ND.py (2019.09.22)
- partial module of a gaming utility for `Romance of The Three Kingdoms II` (KOEI, 1989)
- generate market rate data sample for practicing `gold`-`food` arbitrage
- use `numpy` `matplotlib.pyplot` `scipy`

#### Generate a normal distribution with limited range [25, 75]
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

mu, sigma, n = 50, 10, 1000
llimit, rlimit = 25, 75

data = np.random.normal(mu, sigma, n)
```

#### Method 0. Generating initial data (not trimmed yet)
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
