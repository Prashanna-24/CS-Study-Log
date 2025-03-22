// #include <iostream>
// #include <vector>
// #include <algorithm>
// #include <limits>
// using namespace std;

// int coinChange(vector<int>& coins, int amount) {
//    vector<int> dp(amount + 1, amount + 1);
//    dp[0] = 0;
//    for (int i = 1; i <= amount; i++) {
//       for (int j = 0; j < coins.size(); j++) {
//          if (coins[j] <= i) {
//             dp[i] = min(dp[i], dp[i - coins[j]] + 1);
//          }
//       }
//    }
//    return dp[amount] > amount ? -1 : dp[amount];
// }

// int main() {
//    vector<int> coins = {1, 6, 9, 5};
//    int amount = 10;
//    cout << "Minimum coins needed: " << coinChange(coins, amount) << endl;
//    return 0;
// }

#include <bits/stdc++.h>
using namespace std;

int coinChange(vector<int>& coins, int amount) {
   int n = coins.size();
   vector<vector<int>> dp(n + 1, vector<int>(amount + 1, INT_MAX));

   // Initialize dp[i][0] = 0 (0 coins are needed to make the amount 0)
   for (int i = 0; i <= n; i++) {
      dp[i][0] = 0;
   }

   // Dynamic programming to fill the dp table
   for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= amount; j++) {
         if (coins[i - 1] > j) {
               dp[i][j] = dp[i - 1][j]; // If coin value is greater than the amount, skip it
         } else {
               dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]]);
         }
      }
   }

   // Return the result
   return dp[n][amount] == INT_MAX ? -1 : dp[n][amount];
}

int main() {
   vector<int> coins = {1, 6, 9, 5};  // Example coin denominations
   int amount = 10;                // Example amount
   int result = coinChange(coins, amount);

   if (result != -1)
      cout << "Minimum number of coins required: " << result << endl;
   else
      cout << "Amount cannot be made with the given coins." << endl;

   return 0;
}
