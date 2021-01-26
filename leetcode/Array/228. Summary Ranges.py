'''
用双指针
第一个指针从0出发
第二个指针从1出发
第二个指针每次与前面的一个数字对比 如果发现不是自己-1 的话 就说明我们需要添加东西了
如果i第二个指针之前的数 会等与第一个指针的话 说明没有连续数列 只是单个的数
那么我们就把第一个指针的数字添加进res里面 并且第一个指针指到现在的位置
如果不会等于第一个指针的话 说明 是有一个连续数列的存在的
那么我们就从start 到 第二个指针前一个数 添加进 res里
for循环完成后
我们还需要check 两种情况
首先 如果start 等于 最后一个index的话 说明顺利的走完了 但是 因为是最后一个数 没有机会把最后一个数添加进res里 我们需要把剩下的数添加进res里
还有 如果一直连续的话【1，2，3，4】 永远不会添加进res之中 那么我们就需要把start 到 最后一个数添加进去
'''


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if not nums or len(nums) == 0:return res
        start = 0
        for i in range(1,len(nums)):
            if nums[i]-1 != nums[i-1]:
                if i-1 == start:
                    res.append(str(nums[i-1]))
                else:
                    res.append(str(nums[start]) + "->" + str(nums[i-1]) )
                start = i
        if start == len(nums) - 1:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start]) + "->" + str(nums[len(nums)-1]))
        return res
