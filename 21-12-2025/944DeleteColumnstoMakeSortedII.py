class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        rows,cols=len(strs),len(strs[0])
        ans=0
        flag=False 
        def checkNotSorted(str_1:str,str_2:str):
            return str_1>str_2
        for i in range(rows-1):
            if checkNotSorted(strs[i],strs[i+1]):
                flag=True 
                break 
        if not flag: return 0
        old_chars=[""]*rows 
        for panel in range(cols):
            flag=True 
            for row in range(rows-1):
                if old_chars[row]+strs[row][panel]>old_chars[row+1]+strs[row+1][panel]:
                    flag=False 
                    break 
            if flag:
                for row in range(rows):
                    old_chars[row]+=strs[row][panel]
        return cols-len(old_chars[0])
        

class TestApp:
    def test_case_one(self):
        assert Solution().minDeletionSize(["ca","bb","ac"])==1
    def test_case_two(self):
        assert Solution().minDeletionSize(["xc","yb","za"])==0
    def test_case_three(self):
        assert Solution().minDeletionSize(["zyx","wvu","tsr"])==3
    def test_case_four(self):
        assert Solution().minDeletionSize(["xga","xfb","yfa"])==1
    def test_case_five(self):
        assert Solution().minDeletionSize(["jwkwdc","etukoz"])==2