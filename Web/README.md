# [My Web Practice]
HTML, CSS and JavaScript

- Wedding Anniversary 6 (2021.03.07)
- Wedding Anniversary 5 - 2 (2020.03.11)
- Wedding Anniversary 5 (2020.03.07)
- Colorful Show (2020.03.04)
- Ganzi.html (2017.04.03)


## Wedding Anniversary 6 (2021.03.11)
- Annual Update : change images of the heart and number
- Seperate css id `name` to `name1` and `name2`
- Enhancement of Javascript : use `for` statement

#### WeddingAnniversary6.html
```js
function changeColor() {

	const randNumDec = []; 	// for containing random numbers decimally
	const randNumHex = []; 	// for containing converted numbers hexdecimally
	const cssIdList = ["name1", "name2", "chameleon1", "chameleon2"]; // css id list to change colors

	for (let i = 0; i < 4 ; i++) {
		randNumDec[i] = Math.floor(Math.random() * Math.pow(256, 3)); // generate RGB color (decimal)
		randNumHex[i] = randNumDec[i].toString(16); // turn to the hexdecimal
		document.getElementById(cssIdList[i]).style.color = '#' + randNumHex[i]; // style-color requires #XXXXXX
	}

}

setInterval(changeColor, 500);
```

#### Result
![Wedding Anniversary 6](./Image/2021-03-07%20Wedding%20Anniversary%206.gif)


## Wedding Anniversary 5 - 2 (2020.03.11)
- Enhancement of `vertical-align` between text and image

#### WeddingAnniversary5_2.html
```html
<!DOCTYPE html>

<html>

<head>
	<meta charset="EUC-KR">
	<title>Wedding Anniversary 2</title>
  	<link rel="stylesheet" href="WeddingAnniversary2.css">
</head>

<body>
	<div id='name'>
		K R
		<div id='heart'>
			<img src="heart.gif">
		</div>
		E Y
	</div>
	<div id='chameleon1'>
		Celebrate Our
		<div id='year'>
			<img src="5.gif">
		</div>
		th
	</div>
	<div id='chameleon2'>
		Wedding Anniversary
	</div>
  	<script src="WeddingAnniversary.js">
	</script> 
</body>

</html>
```

#### WeddingAnniversary5.css
```css
@charset "EUC-KR";

#name {
	text-align: center;
	font-family: "Times New Roman", Times, serif;
	font-size: 700%;
}

#chameleon1 {
	text-align: center;
	font-family: "Times New Roman", Times, serif;
	font-size: 550%;
}

#chameleon2 {
	text-align: center;
	font-family: "Times New Roman", Times, serif;
	font-size: 550%;
}

#heart {
	display: inline;
}
#heart img {
	width: 80px;
	height: auto;
}

#year {
	display: inline;
}
#year img {
	vertical-align: -20px;
	width: 100px;
	height: auto;
}
```

#### Result
![Wedding Anniversary 5 - 2](./Image/2020-03-11%20Wedding%20Anniversary%205_2.gif)


## Wedding Anniversary (2020.03.07)
- Application of Colorful Show

#### Result
![Wedding Anniversary](./Image/2020-03-07%20Wedding%20Anniversary%205.gif)


## Colorful Show (2020.03.04)
This is a colorful 'Show'.

#### ColorfulShow.html
```html
<!DOCTYPE html>

<html>

<head>
	<meta charset="EUC-KR">
	<title>Colorful Show</title>
  	<link rel="stylesheet" href="ColorfulShow.css">
</head>

<body>
	<p id='chameleon'>Show</p>
  	<script src="ColorfulShow.js">
		<!--
			<script> can be located in <head> or <body>. 
			But, in this case, we should consider execution sequence.
		-->
		
	</script> 
</body>

</html>
```

#### ColorfulShow.css
```css
@charset "EUC-KR";

#chameleon {
	text-align: center;
	font-family: "Times New Roman", Times, serif;
	font-size: 1000%;
}
```

#### ColorfulShow.js
```javascript
function changeColor() {
	randNumDec = Math.floor(Math.random() * Math.pow(256, 3));
		/*
		 * Math.random() returns a number lower than 1.
	 	 * Math.floor() returns the largest integer less than or equal to a given number.
		 * 256**3 is for the RGB color range between #000000 ~ #FFFFFF.
		 */
	randNumHex = randNumDec.toString(16); /* Convert Decimal to Hexadecimal */

	/* document.write(randNumHex, "<br>"); */
		/* document.write() returns real HTML codes. */
		/* document.write(typeof randColor);
		 * string
		 */

	document.getElementById('chameleon').style.color = '#' + randNumHex;
}

setInterval(changeColor, 1000);
```

#### Result
![Colorful Show](./Image/2020-03-05-23%20Colorful-Show.gif)


## Ganzi.html (2017.04.03)
- A simple Javascript practice

```html
<div id ="Zure">Ganzi</div>

<script type="text/javascript">
  
function thunder() {
	var x = document.getElementById("Zure");
	var storm = document.write(x.innerHTML + " Storm");
	Zure.replace(x,storm);
}
setInterval(thunder, 3000);
	
</script>
```
