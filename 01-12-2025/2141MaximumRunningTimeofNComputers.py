class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        time=0 
        batteries.sort(reverse=True)
        while True:
            right=n-1
            if batteries[right]==0:
                print(time)
                return time 
            ptr=0
            while ptr<=right:
                  batteries[ptr]-=1
                  ptr+=1
            batteries.sort(reverse=True)
            time+=1
class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        low,high=1,sum(batteries)//n 
        while low<high:
            target=high-(high-low)//2 
            extra_time=0
            for power in batteries:
                extra_time+=min(power,target)
            if extra_time//n>=target:
                low=target 
            else:
                high=target-1
        return low
class TestApp:
    def test_case_one(self):
        assert Solution().maxRunTime(2,[3,3,3])==4
    def test_case_two(self):
        assert Solution().maxRunTime(2,[1,1,1,1])==2
    def test_case_three(self):
        assert Solution().maxRunTime(9,[18,54,2,53,87,31,71,4,29,25])==6