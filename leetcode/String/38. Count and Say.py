'''
两个指针
指针pre 记录之前的 数字 并且检查与下一个指针的元素是不是一样的
然后count 记录的是pre 出现了几次 如果发现之前的元素跟下一个元素是相同的 那就+1
发现pre跟现在元素不同时 说明之前元素统计已经结束 可以添加进新的字符串之中了
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if not n:
            return ""
        string = "1"
        for i in range(n-1):
            pre = ","
            count = 0
            new = ""
            for index in string:
                if pre == "," or pre == index:
                    count+=1
                else:
                    new += str(count) +pre
                    count = 1
                pre = index
            new += str(count) + pre
            string = new
        return string
