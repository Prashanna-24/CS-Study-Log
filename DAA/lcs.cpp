#include <bits/stdc++.h>
using namespace std;

int lcs(const string &x, const string &y, string &lcs_string)
{
   int m = x.size();
   int n = y.size();
   vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

   // Fill the dp table
   for (int i = 1; i <= m; ++i)
   {
      for (int j = 1; j <= n; ++j)
      {
         if (x[i - 1] == y[j - 1])
         {
            dp[i][j] = dp[i - 1][j - 1] + 1;
         }
         else
         {
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
         }
      }
   }

   // Trace back from dp[m][n] to get the LCS (ONLY FOR PRINTING THE SEQUENCE)
   int i = m, j = n;
   while (i > 0 && j > 0)
   {
      if (x[i - 1] == y[j - 1])
      {
         lcs_string.push_back(x[i - 1]); // Character is part of LCS
         --i;
         --j;
      }
      else if (dp[i - 1][j] > dp[i][j - 1])
      {
         --i; // Move up
      }
      else
      {
         --j; // Move left
      }
   }

   reverse(lcs_string.begin(), lcs_string.end()); // LCS is constructed in reverse order
   return dp[m][n];
}

int main()
{
   string x = "STONE";
   string y = "LONGEST";
   string lcs_string;

   cout << "Length of LCS: " << lcs(x, y, lcs_string) << endl;
   cout << "LCS: " << lcs_string << endl;
}

// (3d)

// #include <bits/stdc++.h>
// using namespace std;

// // Function to find LCS of three strings
// int lcs3(const string &x, const string &y, const string &z, string &lcs_string)
// {
//    int m = x.size();
//    int n = y.size();
//    int o = z.size();

//    // Create a 3D dp table
//    vector<vector<vector<int>>> dp(m + 1, vector<vector<int>>(n + 1, vector<int>(o + 1, 0)));

//    // Fill the dp table
//    for (int i = 1; i <= m; ++i)
//    {
//       for (int j = 1; j <= n; ++j)
//       {
//          for (int k = 1; k <= o; ++k)
//          {
//                if (x[i - 1] == y[j - 1] && x[i - 1] == z[k - 1])
//                {
//                   dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1;  // Characters match in all three strings
//                }
//                else
//                {
//                   dp[i][j][k] = max({dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1]});  // Take max of the three possibilities
//                }
//          }
//       }
//    }

//    // Trace back to find the LCS string
//    int i = m, j = n, k = o;
//    while (i > 0 && j > 0 && k > 0)
//    {
//       if (x[i - 1] == y[j - 1] && x[i - 1] == z[k - 1])
//       {
//          lcs_string.push_back(x[i - 1]);  // Add the character to the LCS string
//          --i;
//          --j;
//          --k;
//       }
//       else if (dp[i - 1][j][k] >= dp[i][j - 1][k] && dp[i - 1][j][k] >= dp[i][j][k - 1])
//       {
//          --i;  // Move in x's direction
//       }
//       else if (dp[i][j - 1][k] >= dp[i][j][k - 1])
//       {
//          --j;  // Move in y's direction
//       }
//       else
//       {
//          --k;  // Move in z's direction
//       }
//    }

//    reverse(lcs_string.begin(), lcs_string.end());  // LCS is constructed in reverse order
//    return dp[m][n][o];
// }

// int main()
// {
//    string x = "STONE";
//    string y = "LONGEST";
//    string z = "NOTE";
//    string lcs_string;

//    cout << "Length of LCS: " << lcs3(x, y, z, lcs_string) << endl;
//    cout << "LCS: " << lcs_string << endl;

//    return 0;
// }
