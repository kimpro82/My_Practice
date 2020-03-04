function changeColor() {
	randColor = '#' + Math.floor(Math.random() * Math.pow(256, 3));
		/*
			Math.random() returns a number lower than 1.
	 		Math.floor() returns the largest integer less than or equal to a given number.
			256**3 is for the RGB color range between #000000 ~ #FFFFFF.
		*/
	document.write(randColor, "<br>");
		/* document.write() returns real HTML codes. */
	document.write(typeof randColor);
	document.getElementById('chameleon').style.color.disabled
	document.getElementById('chameleon').style.color = randColor;

}

changeColor();
