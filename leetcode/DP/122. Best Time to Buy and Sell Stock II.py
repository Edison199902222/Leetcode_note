

'''
可以用贪心算法 跟dp算
但是贪心算法局限性很大
用两种把 分别写
这道题用dp还是难以理解
'''
class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(len(prices)):
            if i < len(prices)-1 and prices[i+1] > prices[i]:
                profit+=prices[i+1] - prices[i]
        return profit

    def maxProfitOptimizedDP(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        sell = 0
        buy = -prices[0]
        for i in range(1,n):
            sell = max(sell,buy + prices[i]) # 选择继续保持不卖出 还是选择卖出
            buy = max(buy,sell - prices[i]) # 选择不买进 还是买进
        return sell

if __name__ == '__main__':
    solution = Solution()
    list = [1,2,3,4,5]
    print(solution.maxProfit(list))