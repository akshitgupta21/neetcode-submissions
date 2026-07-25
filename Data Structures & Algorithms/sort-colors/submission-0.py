class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=[]
        a=nums.count(0)
        b=nums.count(1)
        c=nums.count(2)
        for i in range(a):
            l.append(0)
        for j in range(b):
            l.append(1)
        for k in range(c):
            l.append(2)
        nums.clear()
        for m in range(len(l)):
            nums.append(l[m])
        return nums

        
        