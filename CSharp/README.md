# My C# Practice
Python seems kind of ugly, but `C#` is the orthodox.
- Overloading (2021.02.02)


## Overloading (2021.02.02)
- a practice of `overloading`

```cs
using System;

class Wife
{

  public string var1, var2;
  public int num1;

  public Wife() {
    Console.WriteLine("우리 마누라는 …… 노코멘트.");
  }

  public Wife(string var1) {
    this.var1 = var1;
    Console.WriteLine("우리 마누라는 " + this.var1 + "입니다.");
  }

  public Wife(string var1, string var2)
  {
    this.var1 = var1;
    this.var2 = var2;
    Console.WriteLine("우리 마누라는 " + this.var1 + "(이)며 " + this.var2 + "입니다.");
  }

  public Wife(int num1) {
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
