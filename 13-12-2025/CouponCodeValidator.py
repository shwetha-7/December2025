import re
class Solution:
    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        res=[]
        map={"restaurant":1,"pharmacy":1,"grocery":1,"electronics":1}
        n=len(isActive)
        arr=[]
        for i in range(n):
            arr.append([code[i],businessLine[i],isActive[i]])
        arr.sort(key=lambda x:(x[1],x[0]))
        for i in range(n):
            if arr[i][0] and arr[i][1] in map and arr[i][2] and self.checkCouponPattern(arr[i][0]):

                res.append(arr[i][0])
        return res
    def checkCouponPattern(self,input:str)->bool:
        res=re.findall(r"[\W]",input)
        return len(res)==0  
Solution().validateCoupons(["1OFw","0MvB"],["electronics","pharmacy"],[True,True])