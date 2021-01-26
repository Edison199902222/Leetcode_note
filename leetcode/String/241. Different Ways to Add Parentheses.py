'''
用递归的方式
先遍历字符串
遇到operator 就拆成两部分递归
然后求出左部分 跟右部分
合并在一起 因为左部分 和右边部分 其实都是list 里面含有很多个数字
然后遍历两个list 相加才是最终结果
'''

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "*-+":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for k in left:
                    for j in right:
                        res.append(self.helper(k,j,input[i]))
        return res
    def helper(self,m,n,op):
        if op == "+":
            return m+n
        if op == "*":
            return m*n
        if op == "-":
            return m-n
if __name__ == "__main__":
    solution = Solution()
    print(solution.diffWaysToCompute("2-1-1"))
