class Solution:
    def climbStairs(n: int) -> int:
        def climb(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 2
            return climb(n - 1) + climb(n - 2)
        
        return climb(n)

for i in range(20):
    print(Solution.climbStairs(i))