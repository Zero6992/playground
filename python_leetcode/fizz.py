class Solution:
    def __init__(self) -> None:
        pass
    
    def fizzBuzz(n) -> list[str]:
        answer = []
        for i in range(1, n+1):
            a = ''
            if (i % 3 == 0):
                a += 'Fizz'
            if (i % 5 == 0):
                a += 'Buzz'
            if a:
                answer.append(a)
            else:
                answer.append(str(i))
        return answer



print(Solution.fizzBuzz(30))
