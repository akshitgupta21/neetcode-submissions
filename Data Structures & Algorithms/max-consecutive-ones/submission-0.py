class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=[]
        a=0
        for i in range(len(nums)):
            if nums[i]==1:
                a+=1
            elif nums[i]==0:
                l.append(a)
                a=0
        l.append(a)
        return max(l)
        