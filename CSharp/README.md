# My C# Practice
Python seems kind of ugly, but `C#` is the orthodox.
- TerminalGUI.cs (2021.03.24)
- Polymorphism.cs (2021.02.18)
- Overloading.cs (2021.02.02)


## TerminalGUI.cs (2021.03.24)
- A practice of `Terminal GUI` from C# using `Terminal.Gui`  
  ☞ https://github.com/migueldeicaza/gui.cs  
- I expected simplicity as much as its appearance, but ……
- Reference  
  https://migueldeicaza.github.io/gui.cs/index.html  
  https://itnext.io/terminal-console-user-interface-in-net-core-4e978f1225b  
  https://sirwan.info/archive/2018/05/02/Developing-Console-based-UI-in-C/  
  https://youtu.be/sVYiDboAe_E
- Terminal Command for installation : `dotnet add package Terminal.Gui`

![Terminal GUI Practice](./image/CSharp%20TerminalGUI%20Output.PNG)

```cs
using System;

namespace TerminalGUI
{
    using Terminal.Gui; 
    class TerminalGUI
    {
        static void Main ()
        {

            Application.Init ();
            var top = Application.Top;

            // Creates the top-level window to show
            // Dynamically computed
            var win = new Window ("Dec ↔ Hex")
            {
                X = 0,
                Y = 1,
                Width = Dim.Fill (),
                Height = Dim.Fill ()
            };

            // Creates a menubar
            var menu = new MenuBar(new MenuBarItem[]
            {
                new MenuBarItem("_File", new MenuItem[]
                {
                    new MenuItem("_Quit", "", () => Application.RequestStop())
                }), // end of file menu
                new MenuBarItem("_Help", new MenuItem[]
                {
                    new MenuItem("_About", "", () 
                    => MessageBox.Query(10, 5, "About", "C# - Terminal GUI Practice\n2021.03.24.", "Ok"))
                }) // end of the help menu
            });

            // Creat contents
            win.Add
            (
                new Label (3, 2, "Decimal    : "),
                new TextField (16, 2, 40, "Enter your number to convert"), // need to declare a variable to contain inputed number
                new Label (3, 4, "Hexdecimal : ")                          // need to print a hexdecimal number converted from input
            );

            top.Add(win, menu);
            Application.Run();

        }
    }
}
```



## Polymorphism.cs (2021.02.18)
- A practice of writing `class` with `abstract` and `sealed` keywords.
- **This code doesn't work.**
- It can't be treated by `try~catch` statement to try instantiating an `abstrat` class or inhreiting `sealed` one.
- Because they belong to `compile-time errors`, not `run-time errors`.
- Compile-time errors must be dealed with by `debugging` process.

#### Codes :
```cs
using System;

abstract class Person
// abstract : can be inherited but can't be instantiated
{
    public Person()
    {
        Console.Write(this + " : ");
    }
}

sealed class MichaelJackson : Person
// sealed : can't be inherited but can be instantiated
{
    public void Say()
    {
        Console.WriteLine("Billie Jean is not my lover.");
    }
}

class BilleJean : MichaelJackson
// An error will occurs because it tries to inherit a sealed class
{
    public void Say()
    {
        Console.WriteLine("You are the one.");
    }
}

class MainClass
{
    static void Main(string[] args)
    {
        try
        {
            new Person();
            // An error will occurs because it tries to be instantiated as an abstract class
        }
        catch (Exception e)
        {
            Console.WriteLine("Abstract class can't be instantiated.");
        }

        new MichaelJackson().Say();

        try
        {
            new BilleJean().Say();
        }
        catch (Exception e)
        {
            Console.WriteLine("MichaelJackson : The kid is not my son");
        }
    }
}
```

#### The results that I mean to get (but impossible because of compiling errors)
> Abstract class can't be instantiated.  
> MichaelJackson : Billie Jean is not my lover.  
> MichaelJackson : The kid is not my son.
 

## Overloading.cs (2021.02.02)
- A practice of `overloading`

```cs
using System;

class Wife
{

  public string var1, var2;
  public int num1;

  public Wife()
  {
    Console.WriteLine("우리 마누라는 …… 노코멘트.");
  }

  public Wife(string var1)
  {
    this.var1 = var1;
    Console.WriteLine("우리 마누라는 " + this.var1 + "입니다.");
  }

  public Wife(string var1, string var2)
  {
    this.var1 = var1;
    this.var2 = var2;
    Console.WriteLine("우리 마누라는 " + this.var1 + "(이)며 " + this.var2 + "입니다.");
  }

  public Wife(int num1)
  {
    this.num1 = num1;
    Console.WriteLine("우리 마누라는 " + this.num1 + "살 먹은 여우입니다.");
  }

}


class MainClass
{

  static void Main (string[] args)
  {
    new Wife();
    new Wife("바보");
    new Wife("멍청이", "말미잘");
    new Wife(100);
  }

}
```
> 우리 마누라는 …… 노코멘트.  
> 우리 마누라는 바보입니다.  
> 우리 마누라는 멍청이(이)며 말미잘입니다.  
> 우리 마누라는 100살 먹은 여우입니다.
