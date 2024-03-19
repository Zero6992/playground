class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = 0
        answer = ''
        while (right < len(s)):
            if (s[right] != ' '):
                right += 1
            else:
                right += 1
                answer += s[left:right:][::-1] # 兩次SLICING 先順者跑在逆著跑
                left = right

        answer += ' '
        answer += s[left:right+1:][::-1] 
        return answer[1:]


s = "Let's take LeetCode contest"

test = Solution()

a = test.reverseWords(s)
print(a)