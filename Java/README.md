# My Java Practice
N/A Java BoA~
- MyThread.java (2021.04.13)
- MyDate.java (2021.03.08)


## MyThread.java (2021.04.13)
- A practice of `Multi-Thread`
- Using `java.lang.Thread`

```java
class NumThread extends Thread
{
	public void run()
	{
		for (int i = 0; i <= 26; i++)
		{
			System.out.print(i);
			try
			{
				Thread.sleep(250);				
			}
			catch (Exception e) {}
		}
	}
}
```

```java
class CharThread extends Thread
{
	public void run()
	{
		for (char letter = 'A'; letter <='Z' ; letter++)
		{
			System.out.print(letter);
			try
			{
				Thread.sleep(250);				
			}
			catch (Exception e) {}
		}
	}
}
```

```java
public class MyThread
{
	public static void main(String args[])
	{
		Thread thread1 = new NumThread();
		Thread thread2 = new CharThread();
		thread1.start();
		thread2.start();
	}
} 
```

> 0A1B2C3D4E5F6G7H8I9J10K11L12M13N14O15P16Q17R18S19T20U21V22W23X24Y25Z26


## MyDate.java (2021.03.08)
- A practice of **deprecated** class `java.util.Date`
- So terrible

```java
import java.util.Date;
import java.text.SimpleDateFormat;
```

```java
		// java.util.Date() : old-fashioned class (deprecated)
		Date date = new Date();
		System.out.println(date); // original
		System.out.println(date.toLocaleString()); // print in Korean
		System.out.println(date.getYear() + 1900); // the year represented by this date, minus 1900
		System.out.println(date.getDay()); // int, 0 = Sunday
```
> Tue Mar 09 09:37:35 KST 2021  
> 2021. 3. 9 �삤�쟾 9:37:35  
> 2021  
> 2

```java
		// set a date
		Date date2 = new Date(2015-1900, 3-1, 7); // month : 0 = January
		System.out.println("\n" + date2);
		System.out.println(date2.getYear() + date2.getMonth() + date2.getDate()); // int + int + int
		// System.out.println(date2.getYear().toString() + date2.getMonth().toString() + date2.getDate().toString()); // error
		System.out.println(date2.getYear() + " " + date2.getMonth() + " " + date2.getDate());
		System.out.println((date2.getYear() + 1900) + "-" + (date2.getMonth() + 1) + "-" + date2.getDate());
```
> Sat Mar 07 00:00:00 KST 2015  
> 124  
> 115 2 7  
> 2015-3-7

```java
		// set a date format
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-mm-dd");
		System.out.println("\n" + sdf.format(date2));
		SimpleDateFormat sdf2 = new SimpleDateFormat("yyyy-MM-dd");
		System.out.println(sdf2.format(date2)); // crazy
```
> 2015-00-07  
> 2015-03-07

```java
		// minus(-) operation between two times different to each other
		long dateDiff = date.getTime() - date2.getTime();
		System.out.println("\nIt has been " + dateDiff/1000/60/60/24 + " days since we got married.");
		// 1 from getTime() means 1/1,000 second
```
> It has been 2194 days since we got married.
