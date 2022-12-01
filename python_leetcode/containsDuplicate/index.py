class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        check = set()
        for i in nums:
            check.add(i)
        originLen = len(nums)
        setLen = len(check)
        if originLen == setLen:
            return False
        return True

nums = [1,3,5,4,2]
test = Solution()

ans = test.containsDuplicate(nums) 

print(ans)