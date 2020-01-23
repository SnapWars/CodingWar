class Solution:
    def reverse(self, x: int) -> int:
        answer = None
        if x < 0:
            answer = int('-' + str(x)[1:][::-1])
        else:
            answer = int(str(x)[::-1])

        return answer if -2**31 < answer < 2**31 - 1 else 0
