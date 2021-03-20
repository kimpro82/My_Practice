# My C# Practice
Python seems kind of ugly, but `C#` is the orthodox.
- ConsoleUI.cs (2021.03.20)
- Polymorphism.cs (2021.02.18)
- Overloading.cs (2021.02.02)


## ConsoleUI.cs (2021.03.20)
- A practice of `console UI` from C#

```cs

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
