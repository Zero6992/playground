class Solution:
    def __init__(self) -> None:
        pass
    def sortColors(nums: list[int]) -> None:
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if(nums[i] > nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
            
        return        
         

testCase = [2,0,2,1,1,0]

Solution.sortColors(testCase)
print(testCase)