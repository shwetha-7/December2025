class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        temp=[[0,0] for _ in range(n+1)]
        for i in range(1,n+1):
            if customers[i-1]=='N':
                temp[i][0]=1
            temp[i][0]+=temp[i-1][0]
        for i in range(n-1,-1,-1):
            if customers[i]=='Y':
                temp[i][1]=1
            temp[i][1]+=temp[i+1][1] 
        index=penalty=n 
        for i in range(n+1):
            sum=temp[i][0]+temp[i][1]
            if sum<=penalty:
                if penalty==sum:
                    index=min(index,i)
                else:
                    index=i
                penalty=temp[i][0]+temp[i][1]
                
        return index 

class TestApp:
    def test_case_one(self):
        assert Solution().bestClosingTime("YYNY")==2
    def test_case_two(self):
        assert Solution().bestClosingTime("NNNNN")==0
    def test_case_three(self):
        assert Solution().bestClosingTime("YYYY")==4    
    def test_case_four(self):
        assert Solution().bestClosingTime("YNYY")==4         