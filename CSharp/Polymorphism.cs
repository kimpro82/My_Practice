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
// An error will occurs because it try to inherit a sealed class
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
            // An error will occurs because it try to be instantiated as an abstract class
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
