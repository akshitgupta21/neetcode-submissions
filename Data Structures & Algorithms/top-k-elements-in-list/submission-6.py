class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[]
        ans=[]
        s=list(set(nums))
        for i in range(len(s)): 
            l.append(nums.count(s[i])) 
        for j in range(k):
            a=l.index(max(l))
            ans.append(s[a])
            l[a]=-1
        return ans



            




            
            
            
        