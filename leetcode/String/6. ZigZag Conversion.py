'''
先创建好zigzag
然后 用row来表示在哪个row要加东西 step表示是+还是-
如果row 是 《 nums的话 继续加1 如果不是 则需要- n
'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(numRows) == 1 or len(numRows) > len(s):
            return s
        zigzag = ["" for i in range(numRows)]
        row,step = 0,1
        for i in s:
            zigzag[row] += i
            if row == 0:
                step = 1
            elif row == numRows-1:
                step = -1
            row+=step
        return "".join(zigzag)