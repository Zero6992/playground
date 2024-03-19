class Solution:
    def maxSubArray(self, nums: list) -> int:
        currentValue = nums[0]
        maxValue = nums[0]
        length = len(nums)
        for i in range(1, length):
            currentValue += nums[i]
            if nums[i] > currentValue:
                currentValue = nums[i]
            if currentValue > maxValue:
                maxValue = currentValue
        
        return maxValue


nums = [-2,1,-3,4,-1,2,1,-5,4]


test = Solution()
ans = test.maxSubArray(nums)

print(ans)