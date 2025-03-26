#include <iostream>
#include <limits.h>
#include <vector>
using namespace std;

int matrix_chain_order(vector<int> p)
{
   int n = p.size() - 1;
   vector<vector<int>> m(n, vector<int>(n, 0));
   vector<vector<int>> s(n, vector<int>(n, 0));
   for (int i = 0; i < n; i++)
   {
      m[i][i] = 0;
   }
   for (int l = 2; l <= n; l++)
   {
      for (int i = 0; i <= n - l; i++)
      {
         int j = i + l - 1;
         m[i][j] = INT_MAX;
         for (int k = i; k < j; k++)
         {
            int q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1];
            if (q < m[i][j])
            {
               m[i][j] = q;
               s[i][j] = k;
            }
         }
      }
   }

   for (int i = 0; i < s.size(); ++i)
   {
      for (int j = 0; j < s[i].size(); ++j)
      {
         cout << s[i][j] << " "; // Print each element in the row
      }
      cout << endl; // Newline after each row
   }
   return m[0][n - 1];
}

int main()
{
   // vector<int> matrix = {30, 35, 15, 5, 10, 20, 25};
   vector<int> matrix = {5, 4, 6, 2, 7};
   int ans = matrix_chain_order(matrix);
   cout << ans;
}