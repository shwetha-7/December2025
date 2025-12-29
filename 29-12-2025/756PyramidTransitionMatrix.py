from collections import defaultdict
class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        map=defaultdict(list)
        for a,b,c in allowed:
            map[a+b].append(c)
        seen=set()
        def dfs(bottom:str,row:str,i:int):
            n=len(bottom)
            if n==1: return True
            if i==n:
                if row in seen: return False 
                seen.add(row)
                return dfs(row,"",1)
            pair=bottom[i-1]+bottom[i]
            for curr in map[pair]:
                if dfs(bottom,row+curr,i+1): return True 
            return False 
        return dfs(bottom,"",1)
class TestApp:
    def test_case_one(self):
        assert Solution().pyramidTransition("BCD",["BCC","CDE","CEA","FFF"])==True 
    def test_case_two(self):
        assert Solution().pyramidTransition("AAAA",["AAB","AAC","BCD","BBE","DEF"])==False