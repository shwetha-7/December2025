from collections import defaultdict

class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        freqPrev=defaultdict(list)
        freqNext=defaultdict(list)
        mod=10**9+7
        n=len(nums)
        for i in range(n-1,0,-1):
            freqNext[nums[i]].append(i)
        count=0
        freqPrev[nums[0]].append(0)
        for i in range(1,n-1):
            curr=nums[i]*2
            if nums[i] in freqNext:
                if freqNext[nums[i]][-1]==i :
                    freqNext[nums[i]].pop()
                    if not freqNext[nums[i]]:
                       del freqNext[nums[i]]
            if curr in freqNext and curr in freqPrev and freqPrev[curr][-1]<i<freqNext[curr][0]:
                count=(count+len(freqPrev[curr])*len(freqNext[curr]))%mod
            freqPrev[nums[i]].append(i)
        return count 
    
Solution().specialTriplets([6,3,6])

class TestApp:
    def test_case_one(self):
        assert Solution().specialTriplets([6,3,6])==1
    def test_case_two(self):
        assert Solution().specialTriplets([0,1,0,0])==1
    def test_case_three(self):
        assert Solution().specialTriplets([8,4,2,8,4])==2
    def test_case_four(self):
        assert Solution().specialTriplets([84,2,93,1,2,2,26])==2
    def test_case_five(self):
        assert Solution().specialTriplets([56,56,87,28,55,56,94])==2
                
