#include <iostream>
#include <cmath>
using namespace std;

long long karatsuba(long long x, long long y)
{
   // Base case for recursion
   if (x < 10 || y < 10)
   {
      return x * y;
   }

   // Calculate the number of digits in the largest number
   int n = max((int)log10(x) + 1, (int)log10(y) + 1);
   int half = n / 2;

   // Split x and y into two halves
   long long a = x / pow(10, half);            // Left part of x
   long long b = x % (long long)pow(10, half); // Right part of x
   long long c = y / pow(10, half);            // Left part of y
   long long d = y % (long long)pow(10, half); // Right part of y

   // Recursive calls
   long long ac = karatsuba(a, c); // Multiply left halves
   long long bd = karatsuba(b, d); // Multiply right halves
   long long ad_plus_bc = karatsuba(a + b, c + d) - ac - bd;

   // Return the final result
   return ac * pow(10, 2 * half) + (ad_plus_bc * pow(10, half)) + bd;
}

int main()
{
   long long x, y;
   cout << "Enter two numbers: ";
   cin >> x >> y;
   cout << "Karatsuba result: " << karatsuba(x, y) << endl;
   return 0;
}
