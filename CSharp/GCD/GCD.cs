using System;
using System.Linq;  // for .Select()

// I hate math.

namespace GCD       // Greatest Common Divisor by Euclidean Algorithm
{
    class MainClass
    {
        static void Main(string[] args)
        {

            Console.Write("Enter two integers : "); // .Write : no line-break
            int[] input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int a = input[0];
            int b = input[1];

            int max = Math.Max(a, b);
            int min = Math.Min(a, b);
            int mod = max;

            int i = 0;
            while(mod != 0)
            {
                mod = max % min;
                Console.WriteLine("{0} : {1} {2} {3}", ++i, max, min, mod); // test
                max = min;
                min = mod;
            } // gcd = max when escape while loop

            Console.WriteLine("GCD : {0}", max);

        }
    }
}