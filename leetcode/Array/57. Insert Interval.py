'''
想法：我们首先要找到 要插入的起点到底是什么
因为这是按照第一个数字 的顺序排好的
所以 如果这个internval 的end 都小于我们的start 说明我们跟这个interval 无交集
找到了之后 并且要检查 是不是这个index 是不是等于我们的length 因为有可能 这个interval 永远跟我们的插入的没关系
找到了从哪里开始有关系了之后 我们的start 要取 跟 这个interval start点的最小值
然后我们找 end
如果我们的end 大于 interval的start的话 说明我们就有关系 再取 我们interval 跟 有关系interval end的最大值

'''

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        length = len(intervals)
        newstart = newInterval[0]
        newend = newInterval[1]
        res = []
        index = 0
        while index < length and intervals[index][1] < newstart:
            res.append(intervals[index])
            index+=1

        if index == length:
            res.append(newInterval)
            return res
        newstart = min(intervals[index][0],newstart)
        while index < length and intervals[index][0] <= newend:
            newend = max(intervals[index][1],newInterval[1])
            index+=1
        res.append([newstart,newend])
        while index < length:
            res.append(intervals[index])
            index+=1
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.insert([[1,3],[6,9]],[2,5]))