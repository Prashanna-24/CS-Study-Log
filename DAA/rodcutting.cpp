// #include<bits/stdc++.h>
// using namespace std;

// int rod_cutting(const vector<int>& prices)
// {
//    int n = prices.size();
//    vector<int> dp(n+1,0);

//    for(int i=1;i<=n;i++)
//    {
//       int max_value = 0;
//       for(int j=0;j<i;j++)
//       {
//          max_value = max(max_value,prices[j] + dp[i-j-1]);
//       }
//       dp[i] = max_value;
//    }
//    return dp[n];
// }
// int main()
// {
//    vector<int> prices = {1, 5, 8, 9, 10, 17, 17, 20};
//    // vector<int> prices = {2,5,7,8};
//    int profit = rod_cutting(prices);
//    cout<<profit;
// }

#include <iostream>
#include <vector>
using namespace std;

/* Returns the best obtainable price for a 
rod of length n and price as prices of 
different pieces */
int cutRod(vector<int>& price, int n) {
   // Create a 2D dp array to store the maximum 
   // revenue obtainable for each length
   vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));

   // Build the dp array in a bottom-up manner
   for (int i = 1; i <= n; i++) {  // For each length
      for (int j = 0; j <= n; j++) { // For each piece
         if (j >= i) {
               // Choose the maximum of including the piece or not
               dp[i][j] = max(price[i - 1] + dp[i][j - i], dp[i - 1][j]);
         } else {
               // If the piece is longer than the current length, just carry forward the previous value
               dp[i][j] = dp[i - 1][j];
         }
      }
   }

   return dp[n][n];
}

/* Driver program to test above functions */
int main() {
   vector<int> price = {1, 5, 8, 9, 10, 17, 17, 20}; // Prices for lengths 1 to 7
   int n = price.size(); // Exclude the price for length 0
   cout << "Maximum obtainable price: " << cutRod(price, n) << endl;
   return 0;
}
