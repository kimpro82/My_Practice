# My Java Practice
N/A Java Boa~
- Swing.java (2021.04.06)
- MyDate.java (2021.03.08)


## Swing.java (2021.04.06)
- A practice of Java `Swing` GUI

![Swing Practice](./Images/Swing.PNG)

#### Import classes
```java
import java.awt.GridLayout;
import javax.swing.*;
import javax.swing.tree.DefaultMutableTreeNode;
```

#### A frame to contain components
```java
		// JFrame : initialize a window
		JFrame f = new JFrame("My Java Swing GUI Practice");

		// (Swing components)
		
		f.setSize(600, 600);
		f.setLayout(new GridLayout(3, 3));
		f.setVisible(true);
```

#### Components
```java
		// JLabel()
		JLabel l1 = new JLabel("This is a text label.");
		l1.setHorizontalAlignment(JLabel.CENTER);
		f.add(l1);
```
```java
		// JTextField
		JTextField t1 = new JTextField("This is a text field.");
		t1.setHorizontalAlignment(JLabel.CENTER);
		f.add(t1);
```
```java
		// JButton
		JButton b1 = new JButton("OK");
		f.add(b1);
```
```java
		//JList
		String gui[] = {"Windows Forms", "WPF", "Electron", "React Native", "Java Swing"};
		JList<String> list = new JList(gui);
		f.add(list);
```
```java
		// JTable
		String data[][] =
		{
			{"Python", "aphoristic"},
			{"C++", "hostile"},
			{"Java", "too much talker"}
		};
		String varname[] = {"Name", "Character"};
		JTable table = new JTable(data, varname);
		f.add(table);
```
```java
		// JTree
		DefaultMutableTreeNode node = new DefaultMutableTreeNode("Java");
		DefaultMutableTreeNode node100 = new DefaultMutableTreeNode("Javax"); node.add(node100);
		DefaultMutableTreeNode node110 = new DefaultMutableTreeNode("Swing"); node100.add(node110);
		DefaultMutableTreeNode node111 = new DefaultMutableTreeNode("JLabel"); node110.add(node111);
		DefaultMutableTreeNode node112 = new DefaultMutableTreeNode("JTextField"); node110.add(node112);
		DefaultMutableTreeNode node113 = new DefaultMutableTreeNode("JButton"); node110.add(node113);
		DefaultMutableTreeNode node200 = new DefaultMutableTreeNode("awt"); node.add(node200);
		DefaultMutableTreeNode node210 = new DefaultMutableTreeNode("GridLayout"); node200.add(node210);	
		JTree tree = new JTree(node);
		f.add(tree);
```
```java
		// JSpinner
		JSpinner spinner = new JSpinner();
		f.add(spinner);
```
```java
		// JSlider
		JSlider slider = new JSlider(JSlider.HORIZONTAL);
		f.add(slider);
```
```java
		// JMenuBar / JMenu
		JMenuBar menuBar = new JMenuBar();
		JMenu fileMenu = new JMenu("File"); menuBar.add(fileMenu);
		JMenu menuItem1 = new JMenu("Open"); fileMenu.add(menuItem1);
		JMenu menuItem2 = new JMenu("Save"); fileMenu.add(menuItem2);
		JMenu menuItem3 = new JMenu("Quit"); fileMenu.add(menuItem3);
		JMenu helpMenu = new JMenu("Help"); menuBar.add(helpMenu);
		JMenu menuItem4 = new JMenu("About"); helpMenu.add(menuItem4);
		f.add(menuBar);
```


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
> 2021. 3. 9 오전 9:37:35  
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
