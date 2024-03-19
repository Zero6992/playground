class Solution:
    def majorityElement(self, nums) -> int:
        count = 0
        answer = 0
        for i in nums:
            if(count == 0):
                answer = i
                count += 1
            elif(answer == i):
                count += 1
            else:
                count -= 1
        
        return answer

test = Solution()
nums = [2,2,1,1,1,2,3,3,3,3,3,3,3,2]
a = test.majorityElement(nums)

print(a)