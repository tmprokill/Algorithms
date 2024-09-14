using System.Numerics;

namespace Pow;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine(Pow(2, 15));
    }

    static int Pow (int a, int n)
    {
        int result = 1;
        while (n > 0)
        {
            if (n % 2 == 1)
            {
                result *= a;
            }

            a *= a;
            n /= 2;
        }

        return result;
    }
}