class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        rows,cols=len(strs),len(strs[0])
        count=0
        for j in range(cols):
            for i in range(rows-1):
                if strs[i][j]>strs[i+1][j]:
                    count+=1
                    break 
        return count 

class TestApp:
    def test_case_one(self):
        assert Solution().minDeletionSize(["cba","daf","ghi"])==1
    def test_case_two(self):
        assert Solution().minDeletionSize(["a","b"])==0
    def test_case_three(self):
        assert Solution().minDeletionSize(["zyx","wvu","tsr"])==3