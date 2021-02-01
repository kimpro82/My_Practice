using System;

class Wife
{

  public string var1, var2;
  public int num1;

  public Wife(string var1) {
    this.var1 = var1;
  }

  public Wife(string var1, string var2)
  {
    this.var1 = var1;
    this.var2 = var2;
  }

  public Wife(int num1) {
    this.num1 = num1;
  }

}


class MainClass
{

  static void Main (string[] args)
  {

    Wife Wife1 = new Wife("바보");
    Wife Wife2 = new Wife("멍청이", "말미잘");
    Wife Wife3 = new Wife(100);

    Console.WriteLine("우리 마누라는 " + Wife1.var1 + "입니다.");
    Console.WriteLine("우리 마누라는 " + Wife2.var1 + "(이)며 " + Wife2.var2 + "입니다.");
    Console.WriteLine("우리 마누라는 " + Wife3.num1 + "살 먹은 여우입니다.");

  }

}
