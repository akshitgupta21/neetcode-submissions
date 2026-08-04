class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        for i in nums:
            b=nums.count(i)
            if b>=int(n/2):
                return i

        

        
        

        

            


        
        