'''
我们需要要得到char 首先要用chr
要用n-1 %26 这样才能得到正确的值
其次为什么最后要reverse 因为这样是从后往前取的
'''


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n:
            res.append(chr((n-1)%26 + ord("A")))
            n = (n-1) // 26
        res.reverse()
        return "".join(res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.convertToTitle(28))
