class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        a=len(temperatures)
        l=[]
        for i in range(len(temperatures)):
            diff=0
            for j in range(i,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    diff=j-i
                    l.append(i)
                    result.append(diff)
                    break
        for i in range(a):
            if i not in l:
                result.insert(i,0) 
        
                                                                
        return result
            
                    


        