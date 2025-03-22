#include <bits/stdc++.h>
using namespace std;

int knapsackHighestProfit(vector<int> &weights, vector<int> &profits, int sack_weight, int n){
   vector<vector<int>> grid(n+1, vector<int>(sack_weight+1, 0));

   for(int i=1; i<=n; i++){
      for(int j=1; j<=sack_weight; j++){
         if(weights[i-1] > j){
            grid[i][j] = grid[i-1][j];
         }
         else{
            grid[i][j] = max(grid[i-1][j], profits[i-1] + grid[i-1][j-weights[i-1]]); // bounded
            // grid[i][j] = max(grid[i-1][j], profits[i-1] + grid[i][j-weights[i-1]]); // unbounded
         }
      }
   }
   
   // backtracking (only for bounded)
   int i = n;
   int j = sack_weight;
   while(i>0 && j>0){
      // if(grid[i][j] == grid[i-1][j]){
      //    i--;
      // }
      if(grid[i][j] != grid[i-1][j]){
         cout << grid[i][j] << " " << "weight: " << weights[i-1] << " "<< "profit: " << profits[i-1] << endl;
         j = j-weights[i-1];
      }
      i--;
   }

   return grid[n][sack_weight];
}

int main(){
   vector<int> profits = {1,2,5,6};
   vector<int>  weights = {2,3,4,5};
   int sack_weight = 8;
   int n = weights.size();

   int ans = knapsackHighestProfit(weights, profits, sack_weight, n);
   cout << "maximum profit: " << ans;

   return 0;
}