# algorithm to find n's square root

import random
import math
import matplotlib.pyplot as plt

n = 2 # should be larger than 1

random.seed(20200101)
squareroot = [random.uniform(1, n)]
lowerlimit, upperlimit = 1, n

k = 20 # run loop k times
for i in range(k) :

    square = squareroot[i] ** 2
    print(i+1, squareroot[i], square, square-n)

    if square == n :
        break;
    elif square < n :
        # print("smaller")
        lowerlimit = max(squareroot[i], lowerlimit)
    else :
        # print("larger")
        upperlimit = min(squareroot[i], upperlimit)

    squareroot.append(random.uniform(lowerlimit, upperlimit))

myplot = plt.plot(range(k+1), squareroot)
# myplot.hlines(math.sqrt(n), color="red", linestyle="--") # doesn't work


# practice
random.random()
random.randrange(1,n) # output only integer
random.uniform(1,n) # output float
list(range(10))
