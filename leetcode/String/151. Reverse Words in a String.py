'''
两个指针
从最后面开始
一个指针会指向单词开始 一个指针指向单词结尾
每次遇到空格 添加进res里 并且更新最后一个指针 让它指向新的单词尾部
最后把res 加上 s【：right】 就行
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        left, right = len(s) - 1, len(s)
        res = ""
        while left > 0:
            if s[left] == " ":
                res += s[left + 1:right] + " "
                while s[left] == " ":
                    left -= 1
                right = left + 1
            left -= 1
        return res + s[:right]


if __name__ == "__main__":
    solution = Solution()
    Input = "the sky is blue"
    print(solution.reverseWords(Input))
