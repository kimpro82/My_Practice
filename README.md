## [My_Practice]
- miscellaneous petty works


### Oncoder Official Coding Test
- https://www.oncoder.com/developer/
- The 11th Test (2019.03.16)


### Python_Lesson (2018.11.11~12.16)
- http://learningspoons.com/offline-class/offline-invest/cryptocurrency/


### Python_Class_Test.py (2018.02.07)
- a simple Python Class practice

<pre><code>class MyFirstClass :
    
    def Family(self, name, role):
        print(name, "is a(an)", role, "in my family")

Do = MyFirstClass()

Do.Family("Kim", "Husband")
Do.Family("Shin", "Wife")
Do.Family("Kim", "Future Baby")</code></pre>

I found that a simple class in Python doesn't need stuffs like `__main__`, `__init__` and so on.
What the `__hell__`?

### Nirvana.py (2017.05.15)
- a simple Python practice

<pre><code>death_entropy = 100
my_entropy = 1

while(my_entropy < death_entropy) :
    print(my_entropy)
    my_entropy += 1
print('Nirvana')</code></pre>

### R_Plotting_Fibonacci Tornado.R (2017.05.07)
- generating Fibonacci Series and Fibonacci Coordinates by looping

##### 1. Generating Fibonacci Series
<pre><code>series <- c(1,1)
n <- 1000                                     ## defining the length of the series

for (i in 3:n) {
  series[i] <- series[i-2] + series[i-1]
}

head(series)</code></pre>

##### 2. Skimming the Movement of Fibonacci Coordinates
<pre><code>## The series' flow : (0,0), (1,0), (1,1), (-1,1), (-1,-2), (4,-2), ……

## Each Coordinate's movement :
## 0 : x = 0, y = 0
## 1 : x <- x + 1
## 2 : y <- y + 1
## 3 : x <- x - 2
## 4 : y <- y - 3
## 5 : x <- x + 5</code></pre>

There are 4 types of calculation for coordinates' movement.
It seems possible to be realized by looping.

##### 2-1. How sort the types of calculation?
<pre><code>## type 1 : %% 4 = 1
## type 2 : %% 4 = 2
## type 3 : %% 4 = 3
## type 4 : %% 4 = 4</code></pre>

##### 3. Generating Fibonacci Coordinates by Looping
<pre><code>x <- 0
y <- 0

for (j in 2:n) {
  if (j %% 2 == 1) {
    x[j] <- x[j-1]
    if (j %% 4 == 1) {
      y[j] <- y[j-1] + series[j-1]  ## type 1
    } else {
      y[j] <- y[j-1] - series[j-1]  ## type 3
      }
  }
  else if (j %% 2 == 0) {
    y[j] <- y[j-1]
    if (j %% 4 == 2) {
      x[j] <- x[j-1] + series[j-1]  ## type 2
    } else {
      x[j] <- x[j-1] - series[j-1]  ## type 4
      }
  }
}</code></pre>

##### 3-1. Drawing Plot
<pre><code>windows(width=5, height=5)
plot(x[1:12], y[1:12], type="l", 
     main="Fibonacci Tornado")
abline(h=0, v=0, col="gray", lty=3)</code></pre>

##### Bonus. Seeing it's Aproximate to the Golden Ratio.
<pre><code>fibonacci.ratio <- c()

for (k in 1:n) {
  fibonacci.ratio[k] = series[k+1]/series[k]
}

windows(width=10, height=5)
par(mfrow=c(1,2))
plot(fibonacci.ratio[1:12],  type="l",
     main="Aproxmate to the Golden Ratio")
abline(h=1.618, col="red", lty=3)
plot(log(series[1:12]), type="l", 
     main="Natural Logarithm of Fibonacci Series")</code></pre>


### R_Plotting_RGB.R (2017.04.14)
- showing RGB color data' distribution by several methods in R
- using plot3d(), converting on coordinate plane
- generating RGB data and using sigmoid function


### Ganzi.html (2017.04.03)
- a simple Javascript practice

<pre><code>&ltdiv id ="Zure"&gtGanzi&lt/div&gt

<script type="text/javascript">
  
function thunder() {
	var x = document.getElementById("Zure");
	var storm = document.write(x.innerHTML + " Storm");
	Zure.replace(x,storm);
}
setInterval(thunder, 3000);
	
</script></code></pre>
