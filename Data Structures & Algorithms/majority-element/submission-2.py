class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in nums:
            b=nums.count(i)
            if b>=int(len(nums)/2):
                return i

        

        
        

        

            


        
        