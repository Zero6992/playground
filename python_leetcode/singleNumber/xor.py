class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for x in nums:
            ans ^= x
        return ans
    
number = [4, 1, 2, 1, 2]

ans = Solution()

a = ans.singleNumber(number)

print(a)
