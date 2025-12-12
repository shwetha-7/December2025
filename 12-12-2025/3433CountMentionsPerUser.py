class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        offline={}
        online=[True]*numberOfUsers 
        res=[0]*numberOfUsers
        for event in events:
            event[1]=int(event[1])
        events.sort(key=lambda x:(int(x[1]), x[0] != 'OFFLINE'))
        for event in events:
            name:str=event[0]
            time_stamp:int=int(event[1])
            id:str=event[2]
            if name=="MESSAGE":
                if id=="ALL":
                    for i in range(numberOfUsers):
                       online[i]=True
                       res[i]+=1
                elif id=="HERE":
                    print(offline)
                    for i in range(numberOfUsers):
                        if online[i] and i not in offline:
                            res[i]+=1
                        elif i in offline and offline[i]+60<=time_stamp:
                            res[i]+=1
                            del offline[i]
                            online[i]=True 
                else:
                    id=id.split(" ")
                    for i in id:
                        temp=int(i[2::])
                        online[temp]=True 
                        res[temp]+=1
            else:
                id=int(id)
                online[id]=False
                offline[id]=time_stamp 

        return res 


class TestApp:
    def test_case_one(self):
        assert Solution().countMentions(2,[["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]])==[2,2]
    def test_case_two(self):
        assert Solution().countMentions(2,[["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]])==[2,2]
    def test_case_three(self):
        assert Solution().countMentions(2,[["OFFLINE","10","0"],["MESSAGE","12","HERE"]])==[0,1]
    def test_case_four(self):
        assert Solution().countMentions(3,[["MESSAGE","2","HERE"],["OFFLINE","2","1"],["OFFLINE","1","0"],["MESSAGE","61","HERE"]])==[1,0,2]