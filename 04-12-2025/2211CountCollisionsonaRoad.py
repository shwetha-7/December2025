

class Solution:
    def countCollisions(self, directions: str) -> int:
        stack=[directions[0]]
        count=0
        for i in range(1,len(directions)):
            direction=directions[i]
            if stack and stack[-1]=='R' and direction=='L':
                count+=2
                stack.append("S")
            elif stack and stack[-1]=='S' and direction=='L':
                count+=1
                stack.append("S")
            elif stack and stack[-1]=='R' and direction=='S':
                count+=1
                stack.append(direction)
            else:
                stack.append(direction)
        return count     

class Solution:
    def countCollisions(self, directions: str) -> int:
        left,right=0,len(directions)-1
        while left<len(directions) and directions[left]=='L':
            left+=1
        while right>=0 and directions[right]=='R':
            right-=1
        count=0
        if left<right:
            for i in range(left,right+1):
                count+=1 if directions[i]!='S' else 0 
        return count
class TestApp:
    def test_case_one(self):
        assert Solution().countCollisions("RLRSLL")==5
    def test_case_two(self):
        assert Solution().countCollisions("LLRR")==0
    def test_case_three(self):
        assert Solution().countCollisions("LLRLRLLSLRLLSLSSSS")==10
    def test_case_four(self):
        assert Solution().countCollisions("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR")==20
        
        