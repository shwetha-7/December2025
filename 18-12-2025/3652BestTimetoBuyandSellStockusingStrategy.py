import math
class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        max_profit=0
        n=len(strategy)
        for i in range(n):
            max_profit+=prices[i]*strategy[i]
        res=[0]*n
        for i in range(n-k+1):
            sum=0
            if i>0:
               total=i+k
               start=(total//2)+1
               for j in range(start,total):
                   sum+=prices[j]
            else:
                total=i+k 
                start=1 
                for j in range(start,total):
                    sum+=prices[j]
            res[i]=sum 
        post_compute=[0]*n 
        post_compute[-1]=prices[-1]*strategy[-1]
        for i in range(n-2,-1,-1):
            post_compute[i]=prices[i]*strategy[i]+post_compute[i+1]
        pre_sum=0 
        for i in range(n-k+1):
            if i>0:
                delta=res[i]
                base=post_compute[i+k] if i!=n-k else 0
                max_profit=max(max_profit,delta+base+pre_sum)
                pass 
            else:
                delta=res[i]
                base=post_compute[i+k]
                max_profit=max(max_profit,base+delta)
            pre_sum+=(prices[i]*strategy[i])
        return max_profit
    
class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        n=len(prices)
        profit_sum=[0]*(n+1)
        price_sum=[0]*(n+1)
        for i in range(n):
            profit_sum[i+1]=profit_sum[i]+prices[i]*strategy[i]
            price_sum[i+1]=price_sum[i]+prices[i]
        res=profit_sum[n]
        for i in range(k-1,n):
            left_profit=profit_sum[i-k+1]
            right_profit=profit_sum[n]-profit_sum[i+1]
            change_profit=price_sum[i+1]-price_sum[i-k//2+1]
            res=max(res,left_profit+change_profit+right_profit)     
        return res
class TestApp:
    def test_case_one(self):
        assert Solution().maxProfit([4,2,8],[-1,0,1],2)==10
    def test_case_two(self):
        assert Solution().maxProfit([5,4,3], [1,1,0], 2)==9
    def test_case_three(self):
        assert Solution().maxProfit([5,14,16,9],[-1,0,0,-1],2)==5