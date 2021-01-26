
'''
这道题 先把列表从大到小sort
sort完以后
如果 index位置上的数字大于index+1 说明我们大于或者等于h的文章+1

'''

class Solution:
    def hIndex(self, citations) -> int:
        if not list:return 0
        h = 0
        citations = sorted(citations, reverse = True)
        for i in range(0,len(citations)):
            if citations[i] >= i+1:
                h = i+1
        return h
if __name__ =="__main__":
    solution = Solution()
    print(solution.hIndex([3,0,6,1,5]))