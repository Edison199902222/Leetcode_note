'''
这道题
sums 记录 总共车走完全程 从第一个到最后一个 剩下多少汽油 如果大于等于0 说明肯定可以走完
current 意思是 走到第i个站 有多少汽油
如果 剩下的汽油 加上第i个站的汽油 小于下个站的汽油的话 说明走不过去了 需要跳过
'''
class Solution(object):
    def canCompleteCircuit(self,gas,cost):
        if sum(gas) - sum(cost) < 0:
            return -1
        sums,current,index = 0,0,0
        for i in range(len(gas)):
            if (current+gas[i]) < cost[i]:
                index = i+1
                current = 0
            else:
                current = current + gas[i] - cost[i]
                sums+=gas[i]-cost[i]
        if sums >= 0:
            return index
        else:
            return -1

if __name__ == "__main__":
    solution = Solution()
    gas = [5,1,2,3,4]
    cost = [4,4,1,5,1]
    print(solution.canCompleteCircuit(gas,cost))