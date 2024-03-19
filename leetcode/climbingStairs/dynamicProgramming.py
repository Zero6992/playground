class Solution:
    def climbStairs(n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp1, dp2 = 1, 2
        for _ in range(n - 2):
            dp1, dp2 = dp2, dp1 + dp2
        
        return dp2
    
for i in range(20):
    print(Solution.climbStairs(i))