class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l=[]
        c=nums.copy()
        d=len(c)
        a=0
        while a!=d:
            b=min(nums)
            l.append(b)
            nums.remove(b)
            a+=1
        nums.clear()
        nums=l
        return nums

        



        
            
        