class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        temp = {}
        for x in nums:
            if x in temp:
                del temp[x]
            else:
                temp[x] = 1
        for key in temp:
            ans = key

        return ans

# 如果是陣列只需要將ans改成[], append每個key即可
number = [4, 1, 2, 1, 2]

ans = Solution()

a = ans.singleNumber(number)

print(a)
