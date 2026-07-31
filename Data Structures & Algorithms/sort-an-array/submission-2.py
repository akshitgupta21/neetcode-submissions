class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l=[]
        d=len(nums)
        a=0
        while a!=d:
            b=min(nums)
            l.append(b)
            nums.remove(b)
            a+=1
        nums=l
        return nums

        



        
            
        