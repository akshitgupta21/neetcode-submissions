class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        e=nums.count(0)
        for i in range(e):
            nums.remove(0)
            nums.append(0)
        