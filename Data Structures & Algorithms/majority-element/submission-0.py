class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a={}
        for i in range(len(nums)):
            b=nums.count(nums[i])
            a[nums[i]]=b
        l=list(a.values())
        c=max(l)
        d=0
        for key,value in a.items():
            if value==c:
                return key
        
        

        

            


        
        