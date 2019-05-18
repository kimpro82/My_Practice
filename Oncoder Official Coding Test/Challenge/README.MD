Challenge Tests


## Q1. 문자열 리턴

```Python
class Solution:
    def solution(self, str):
        self.str = str
        return str
```


## Q2. 연산하기

```Python
class Solution:
    def solution(self, a, b):
       self.a = a
       self.b = b
       return a**3 + b**2
```


## Q3. 홀수 짝수 판별

```Python
class Solution:
    def solution(self, a):
        self.a = a
        if a % 2 == 1 :
            return "ODD"
        else :
            return "EVEN"
```


## Q4. 짝수 갯수 구하기  

```Python
class Solution:
    def solution(self, arr):
        self.arr = arr
        n = 0
        for i in list(arr) :
            if i % 2 == 0 :
                n += 1
            else :
                n += 0
        return n
```


## Q5. 13 구하기 

```Python
class Solution:
    def solution(self, a):
        self.a = a
        self.count = 0
        self.mylist = list(range(1,self.a+1))
        
        for i in self.mylist :
            if '13' in str(self.mylist[i-1]) :
                self.count += 1
                
        return self.count
```

### test

```Python
do = Solution()
do.solution(13)
```
> 1

### practice
```Python
a = 13
mylist = list(range(1,a+1))
mylist
mylist[12]
```
> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  
> 13

```Python
type(a)
```
> int

```Python
'13' in str(a)
'13' in str(mylist[11])
'13' in str(mylist[12])
```
> True  
> False  
> True


## Q6. 셀프넘버 판별 
suffered heavy trial and error but shockingly short final output
```Python
class Solution:

    def solution(self, a):
        self.a = a
        self.mysumlist = []
        self.mycount = 0

        for i in list(range(1,self.a+1)) :

            self.mysum = i
            for j in list(range(0,len(str(i)))) :
                self.mysum += int(str(i)[j])

            self.mysumlist.append(str(self.mysum))

        return self.mysumlist.count(str(a))
```

### test
```Python
do = Solution()
do.solution(25)
```
> 1

### practice
```Python
a = 25
print(str(a)[0])
print(str(a)[1])
print(len(str(a)))
```
> 2  
  5  
  2
  
```Python
# Let's master list(range())
print(range(0,len(str(a))))
print(list(range(0,len(str(a))))) # What a magic?

print(list(range(2,3)))
print(list(range(1,3)))
print(list(range(0,3)))
```
> range(0, 2)  
  [0, 1]  

> [2]  
  [1, 2]  
  [0, 1, 2]

```Python
print(str(a)[0] + str(a)[1])
print(a + int(str(a)[0]) + int(str(a)[1]))
```
> 25  
  32

```Python
# loop 1
mylist = []
for i in list(range(1,a+1)) :
    mylist.append(i)
print(mylist)
```
>  [1, 2, 3, 4, …… , 25]

```Python
# loop 2
mysum = a
for j in list(range(0,len(str(a)))) :
    mysum += int(str(a)[j])
print(mysum)
```
> 32

```Python
# using count() method
print(mysum.count(32))
print(str(mysum).count('32'))
```
> AttributeError: 'int' object has no attribute 'count'  
  1

```Python
# loop 1 + 2
mysumlist = []
for i in list(range(1,a+1)) :
    mysum = i
    for j in list(range(0,len(str(i)))) :
        mysum += int(str(i)[j])
        print(i, j, mysum)
    mysumlist.append(str(mysum))
```
> 1 0 2  
  2 0 4  
  (중략)  
  25 1 32

```Python
print(mysumlist)
```
> ['2', '4', '6', …… , '32']

```Python
str(mysumlist).count('32')
```
> 1
