class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        
        
        vector<int> dp = cost;
        int len = cost.size();
        
      
        
        dp.emplace_back(0);
        cost.emplace_back(0);
        
    
        
        for (int i=2; i<len+1; ++i) {
            dp[i] = cost[i] + min(dp[i-1], dp[i-2]);
            
        }
        
        return dp[len];
    }
};
