class Solution:
    def reverseString(self, s) -> None:
      left = 0
      right = len(s) - 1
      while(left < right):
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

      return s



s = ["h","e","l","l","o"]

test = Solution()
s = test.reverseString(s)
print(s)