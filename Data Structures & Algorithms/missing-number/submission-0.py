class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m=max(nums)
        nums.sort()
        a=0
        if len(nums)!=m:
            return m+1
        for i in range(len(nums)):
            if nums[i]==a:
                a+=1
            else:
                return a
        return None
        
        