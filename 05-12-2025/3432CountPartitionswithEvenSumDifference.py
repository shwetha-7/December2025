class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        total=sum(nums)
        count=0
        curr=0
        for num in range(len(nums)-1):
            curr+=num
            total=total-num
            if abs(curr-total)%2==0:
                count+=1
        return count 
            
class TestApp:
    def test_case_one(self):
        assert Solution().countPartitions([10,10,3,7,6])==4
    def test_case_two(self):
        assert Solution().countPartitions([1,2,2])==0
    def test_case_three(self):
        assert Solution().countPartitions([2,4,6,8])==3
        